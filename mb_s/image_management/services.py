from mbs_db.models import ImageFile
from django.urls import reverse
from image_management.image_upload_form import ImageUploadForm
from utils.image_utils import ImageUtils

class ImageManagementServices:
    @staticmethod
    def upload_image(request):
        form = ImageUploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
            for f in files:
                imagefile = ImageFile(model_pic=f)
                imagefile.save()
            context = {"is_upload": True, "message": "upload success", "image_url": imagefile.get_img_url()}
        else:
            context = {"is_upload": False, "message": "upload fail", "image_url": None}
        return context

    @staticmethod
    def delete_test_images():
        image_lists = ImageFile.objects.all()
        image_lists.delete()
        image_dir = "images"
        ImageUtils.update_image_dir(ImageFile, image_dir)
