import os

class ModelUtils:
    @staticmethod
    def update_model_dir(model, model_dir):
        model_list = list(model.objects.values_list('model_path', flat=True))
        dir_list = os.listdir(model_dir)
        for model_name in dir_list:
            model_path = model_dir + "/" + model_name
            if model_path not in model_list:
                os.remove(model_path)
