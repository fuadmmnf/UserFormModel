from django.conf.urls import url
from . import views

app_name = 'user_model'

urlpatterns = [
  # url(r'^$', views.users, name='users'),
  url(r'^$', views.register, name='register')
]