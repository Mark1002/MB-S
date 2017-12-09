import os

class ImageUtils:
    @staticmethod
    def update_image_dir(image_model, image_dir):
        images_list = list(image_model.objects.values_list('model_pic', flat=True))
        dir_list = os.listdir(image_dir)
        for image_name in dir_list:
            image_path = image_dir + "/" + image_name
            if image_path not in images_list:
                os.remove(image_path)
