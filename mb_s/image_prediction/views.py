import logging
from django.shortcuts import render
from django.views import View
from image_prediction.services import ImagePredictServices

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class ImagePredictView(View):
    def get(self, request):
        context = ImagePredictServices.get_prediction_context()
        return render(request, 'image_prediction/prediction.html', context)
    
    def post(self, request):
        pass
