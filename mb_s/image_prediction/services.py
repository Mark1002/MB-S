import cv2
import numpy as np
from mbs_db.models import ImageFile
from keras.models import load_model

class ImagePredictServices:
    @staticmethod
    def run(model_id):
        if ImageFile.objects.count() == 0:
            return None
        image_shape = (150, 150)
        image_list = ImageFile.objects.all()
        test_images = []
        
        for image in image_list:
            image = cv2.imread(image.model_pic.name)
            res = cv2.resize(image, image_shape, interpolation=cv2.INTER_CUBIC)
            test_images.append(res)
        
        test_images = np.array(test_images)
        img_normalize = test_images.astype('float32') / 255
        model_list = [
            {
				"model_name": "男明星",
                "model_path": "model_dir/男明星.h5",
                "label_dict": {'周杰倫': 0, '康康': 1,  '蕭敬騰': 2 ,'鄧佳華': 3, '金城武': 4}
            }, 
            {
				"model_name": "罕見生物",
                "model_path": "model_dir/罕見生物.h5",
                "label_dict": {'鮟鱇魚': 0, '紅唇蝙幅魚': 1,  '高鼻羚羊': 2 ,'藍鸚鵡魚': 3, '鯨頭鸛': 4}
            }
        ]
        model_info = model_list[int(model_id)]
        model = load_model(model_info["model_path"])
        # predict test data
        label_dict = model_info["label_dict"]
        label_dict = dict((v, k) for (k,v) in label_dict.items())
        predict_prob_list = np.round(model.predict(img_normalize), 5)
        predict_label = model.predict_classes(img_normalize)        
        result_list = []
        for i in range(len(predict_prob_list)):
            image_path = image_list[i].get_img_url()
            ans = label_dict[predict_label[i]]
            probs = dict((label_dict[j], predict_prob_list[i][j]) for j in range(len(predict_prob_list[i])))
            result_list.append({"model": model_info["model_name"], "image": image_path, "ans": ans, "probs": probs})

        return result_list
        
    @staticmethod
    def get_prediction_context(result_list=None):
        image_list = ImageFile.objects.all()
        model_list = [{"name": "男明星"}, {"name": "罕見生物"}]
        context = {
            "image_list": image_list, 
            "model_list": model_list,
            "result_list": result_list
        }
        return context
