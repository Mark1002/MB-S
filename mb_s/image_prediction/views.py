import logging
import tensorflow as tf
from django.shortcuts import render
from django.views import View
from image_prediction.services import ImagePredictServices
from keras import  backend as K

graph = tf.get_default_graph()
logger = logging.getLogger(__name__)

class ImagePredictView(View):
    def get(self, request):
        service = ImagePredictServices()
        context = service.get_prediction_context()
        return render(request, 'image_prediction/prediction.html', context)
    
    def post(self, request):
        with graph.as_default():
            service = ImagePredictServices()
            result = service.run(request.POST['model_id'])
        K.clear_session()
        context = service.get_prediction_context(result)
        return render(request, 'image_prediction/prediction.html', context)
