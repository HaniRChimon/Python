from django.conf.urls import url, include

urlpatterns =[
    url(r'^', include('apps.Book_Author_App.urls')),
]
