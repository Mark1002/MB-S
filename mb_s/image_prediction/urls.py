from django.conf.urls import url
from image_prediction import views

app_name = 'image_prediction'
urlpatterns = [
    url(r'^$', views.ImagePredictView.as_view(), name='image_prediction'),
]
