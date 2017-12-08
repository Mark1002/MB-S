from django.conf.urls import url
from image_management import views

app_name = 'image_management'
urlpatterns = [
    url(r'^upload-images/$', views.ImageUploadView.as_view(), name='upload_predict_images'),
    url(r'^images/(?P<img_name>.+)$', views.ImageUrl.as_view(), name='images_url'),
    url(r'^delete-test-images/$', views.DeleteTestImageView.as_view(), name='delete_test_images'),
]
