from django.conf.urls import url
from image_class_management import views

app_name = 'image_class_management'
urlpatterns = [
    url(r'^challenge/(?P<challenge_id>\d+)/imageclass/$', views.ShowImageClassView.as_view(), name='show_image_class'),
    url(r'^challenge/(?P<challenge_id>\d+)/imageclass/add/$', views.AddImageClassView.as_view(), name='add_image_class'),
]
