from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newbook$', views.NewBook),
    url(r'^newauthor$', views.newauthor),
    url(r'^book_info/(?P<number>\d+)$', views.ShowBook),
    url(r'^book/(?P<id>\d+)/remove$', views.RemoveBook),  
    url(r'^viewauthors$', views.ShowAuthor),
    url(r'^author_info/(?P<id>\d+)$', views.viewauthor),
    url(r'^author/(?P<id>\d+)/remove$', views.removeauthor),
    url(r'^addbook/(?P<id>\d+)$', views.addbook),
]