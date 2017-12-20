from mbs_db.models import ModelInfo
from utils.model_utils import ModelUtils

class ModelManagementServices:
    @staticmethod
    def get_all_model():
        model_list = ModelInfo.objects.all()
        return model_list
    
    @staticmethod
    def delete_model_byId(model_id):
        model = ModelInfo.objects.get(pk=model_id)
        model.delete()
        ModelUtils.update_model_dir(ModelInfo, "model_dir")
