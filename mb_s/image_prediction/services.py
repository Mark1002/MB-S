import cv2
import logging
import numpy as np
from mbs_db.models import ImageFile, ModelInfo
from keras.models import load_model

logger = logging.getLogger(__name__)

class ImagePredictServices:
    def get_test_images(self):
        image_query_sets = self.fetch_image_query_sets()
        test_images = []
        for query_set in image_query_sets:
            image = cv2.imread(query_set.model_pic.name)
            test_images.append(image)
        return test_images
    
    def fetch_image_query_sets(self):
        image_query_sets = ImageFile.objects.filter(imageclass_id=0)
        return image_query_sets
        
    def preprocess_test_images(self, test_images):
        image_shape = (150, 150)
        test_images = [cv2.resize(image, image_shape, interpolation=cv2.INTER_CUBIC) for image in test_images]
        test_images = np.array(test_images)
        test_images_normalize = test_images.astype('float32') / 255
        return test_images_normalize
    
    def run(self, model_id):
        test_images = self.get_test_images()
        test_images = self.preprocess_test_images(test_images)
        model_info = ModelInfo.objects.get(pk=model_id)
        model = load_model(model_info.model_path)
        # predict test data
        label_dict = eval(model_info.label_dict)
        label_dict = dict((v, k) for (k,v) in label_dict.items())
        predict_prob_list = np.round(model.predict(test_images), 5)
        predict_label = model.predict_classes(test_images)
        image_query_sets = self.fetch_image_query_sets()        
        result_list = []
        for i in range(len(predict_prob_list)):
            image_path = image_query_sets[i].get_img_url()
            ans = label_dict[predict_label[i]]
            probs = dict((label_dict[j], predict_prob_list[i][j]) for j in range(len(predict_prob_list[i])))
            percent = round(probs[ans]*100, 5)
            result_list.append({"image": image_path, "ans": ans, "percent": percent, "probs": probs})
        logger.info(result_list)
        return result_list[0]
        
    def get_prediction_context(self, result=None):
        image_list = ImageFile.objects.filter(imageclass_id=0)
        model_list = ModelInfo.objects.all()
        logger.info(result)
        context = {
            "image_list": image_list, 
            "model_list": model_list,
            "result": result
        }
        return context
