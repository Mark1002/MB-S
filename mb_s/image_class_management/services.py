from mbs_db.models import Challenge, ImageClass

class ImageClassManagementServices:
    @staticmethod
    def select_image_class(challenge_id):
        imageclass_list = ImageClass.objects.filter(challenge_id=challenge_id)
        return imageclass_list

    @staticmethod
    def select_image_class_byId(imageclass_id):
        imageclass = ImageClass.objects.get(pk=imageclass_id)
        return imageclass

    @staticmethod
    def add_image_class(challenge_id, image_class_name):
        challenge = Challenge.objects.get(pk=challenge_id)
        imageclass = ImageClass(name=image_class_name, challenge=challenge)
        imageclass.save()
    
    @staticmethod
    def delete_image_class(imageclass_id):
        imageclass = ImageClass.objects.get(pk=imageclass_id)
        imageclass.delete()
