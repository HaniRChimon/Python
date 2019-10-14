from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^gen$', views.Gen),
    url(r'^reset$', views.Reset),
]