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
        try:
            with graph.as_default():
                lock.acquire()
                context = ModelTrainingServices.run(challenge_id)
                lock.release()
            K.clear_session()
            return JsonResponse(context) 
        except Exception as e:
            return HttpResponseRedirect(reverse('image_class_management:show_image_class', args=[challenge_id]))

class PollingTrainState(View):
    def get(self, request):
        return JsonResponse({"status": "ok", "isTrain": True})
