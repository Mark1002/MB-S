import logging
from django.shortcuts import render
from django.views import View

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class ImagePredictView(View):
    def get(self, request):
        return render(request, 'image_prediction/prediction.html')
    
    def post(self, request):
        pass
