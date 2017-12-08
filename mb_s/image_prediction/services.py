from mbs_db.models import ImageFile


class ImagePredictServices:
    @staticmethod
    def get_prediction_context():
        image_list = ImageFile.objects.all()
        context = {"image_list": image_list}
        return context
