from django.conf.urls import url
from challenge_management import views

app_name = 'challenge_management'
urlpatterns = [
    url(r'^challenge/$', views.ShowChallengeView.as_view(), name='show_challenge'),
    url(r'^challenge/add/$', views.AddChallengeView.as_view(), name='add_challenge'),
    url(r'^challenge/delete/(?P<challenge_id>\d+)/$', views.DeleteChallengeView.as_view(), name='delete_challenge'),
]
