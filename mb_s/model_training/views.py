import tensorflow as tf
import threading
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from keras import backend as K
from model_training.services import ModelTrainingServices

graph = tf.get_default_graph()
lock = threading.Lock()

class ModelTrainingView(View):
    def post(self, request):
        challenge_id = request.POST['challenge_id']
        with lock:
            try:
                with graph.as_default():
                    context = ModelTrainingServices.run(challenge_id)
                K.clear_session() 
            except Exception as e:
                return HttpResponseRedirect(reverse('image_class_management:show_image_class', args=[challenge_id]))
        return JsonResponse(context)

class PollingTrainState(View):
    def get(self, request):
        is_train = ModelTrainingServices.get_training_state()
        return JsonResponse({"status": "ok", "isTrain": is_train})
