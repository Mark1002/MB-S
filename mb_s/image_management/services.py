from mbs_db.models import ImageClass, ImageFile
from image_management.image_upload_form import ImageUploadForm
from utils.image_utils import ImageUtils

class ImageManagementServices:
    @staticmethod
    def upload_image(request, imageclass_id=None):
        form = ImageUploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
            if imageclass_id is None:
                # limit one image
                ImageManagementServices.delete_test_images()
                for f in files:
                    imagefile = ImageFile(model_pic=f, imageclass_id=0)
                    imagefile.save()
            else:
                imageclass = ImageClass.objects.get(pk=imageclass_id)
                for f in files:
                    imagefile = ImageFile(model_pic=f, imageclass=imageclass)
                    imagefile.save()
            context = {"is_upload": True, "message": "upload success", "image_url": imagefile.get_img_url()}
        else:
            context = {"is_upload": False, "message": "upload fail", "image_url": None}
        return context

    @staticmethod
    def delete_test_images():
        image_lists = ImageFile.objects.filter(imageclass_id=0)
        image_lists.delete()
        image_dir = "images"
        ImageUtils.update_image_dir(ImageFile, image_dir)
