from django.conf.urls import url
from model_training import views

app_name = 'model_training'
urlpatterns = [
    url(r'^model-training/$', views.ModelTrainingView.as_view(), name='model_training'),
]
