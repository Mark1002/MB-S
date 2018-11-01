import tensorflow as tf
import threading
import logging
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from keras import backend as K
from model_training.services import ModelTrainingServices

graph = tf.get_default_graph()
logger = logging.getLogger(__name__)

class ModelTrainingView(View):
    def post(self, request):
        challenge_id = request.POST['challenge_id']
        service = ModelTrainingServices()
        try:
            with graph.as_default():
                t = threading.Thread(target=service.run, args=(challenge_id,))
                t.start()
            K.clear_session()
        except Exception as e:
            logger.info(str(e))
            return HttpResponseRedirect(reverse('image_class_management:show_image_class', args=[challenge_id]))
        return JsonResponse({"status": "ok", "challenge_id": challenge_id})

class PollingTrainState(View):
    def get(self, request):
        is_train = ModelTrainingServices.get_training_state()
        return JsonResponse({"status": "ok", "isTrain": is_train})
