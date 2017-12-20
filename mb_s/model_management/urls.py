from django.conf.urls import url
from model_management import views

app_name = 'model_management'
urlpatterns = [
    url(r'^model-management/$', views.ShowModelView.as_view(), name='show_model'),
    url(r'^model-management/delete/$', views.DeleteModelView.as_view(), name='delete_model'),
]
