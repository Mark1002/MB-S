import tensorflow as tf
from django.http import HttpResponseRedirect
from django.urls import reverse
from keras import backend as K
from django.views import View
from django.shortcuts import render
from model_training.services import ModelTrainingServices

graph = tf.get_default_graph()

class ModelTrainingView(View):
    def post(self, request):
        challenge_id = request.POST['challenge_id']
        try:
            with graph.as_default():
                ModelTrainingServices.run(challenge_id)
            K.clear_session()
            return HttpResponseRedirect(reverse('image_class_management:show_image_class', args=[challenge_id]))
        except Exception as e:
            return HttpResponseRedirect(reverse('image_class_management:show_image_class', args=[challenge_id]))
