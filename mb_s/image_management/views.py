import logging
import os
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.static import serve
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from image_management.services import ImageManagementServices

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class ImageUploadView(View):
    def post(self, request):
        context = ImageManagementServices.upload_image(request)
        return JsonResponse(context)

class ImageUrl(View):
    def get(self, request, img_name):
        path = os.getcwd() + "/images/" + img_name
        return serve(request, os.path.basename(path), os.path.dirname(path))

class DeleteTestImageView(View):
    def get(self, request):
        return render(request, 'image_management/delete_test_image.html')
    
    def post(self, request):
        ImageManagementServices.delete_test_images()
        return HttpResponseRedirect(reverse('image_prediction:image_prediction'))
