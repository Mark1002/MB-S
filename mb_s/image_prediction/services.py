import cv2
import numpy as np
from mbs_db.models import ImageFile, ModelInfo
from keras.models import load_model

class ImagePredictServices:
    @staticmethod
    def run(model_id):
        image_list = ImageFile.objects.filter(imageclass_id=0)
        if  image_list.count() == 0:
            return None
        image_shape = (150, 150)
        test_images = []
        for image in image_list:
            image = cv2.imread(image.model_pic.name)
            res = cv2.resize(image, image_shape, interpolation=cv2.INTER_CUBIC)
            test_images.append(res)
        
        test_images = np.array(test_images)
        img_normalize = test_images.astype('float32') / 255
        model_info = ModelInfo.objects.get(pk=model_id)
        model = load_model(model_info.model_path)
        # predict test data
        label_dict = eval(model_info.label_dict)
        label_dict = dict((v, k) for (k,v) in label_dict.items())
        predict_prob_list = np.round(model.predict(img_normalize), 5)
        predict_label = model.predict_classes(img_normalize)        
        result_list = []
        for i in range(len(predict_prob_list)):
            image_path = image_list[i].get_img_url()
            ans = label_dict[predict_label[i]]
            probs = dict((label_dict[j], predict_prob_list[i][j]) for j in range(len(predict_prob_list[i])))
            percent = round(probs[ans]*100, 5)
            result_list.append({"image": image_path, "ans": ans, "percent": percent, "probs": probs})

        return result_list[0]
        
    @staticmethod
    def get_prediction_context(result=None):
        image_list = ImageFile.objects.filter(imageclass_id=0)
        model_list = ModelInfo.objects.all()
        context = {
            "image_list": image_list, 
            "model_list": model_list,
            "result": result
        }
        return context
