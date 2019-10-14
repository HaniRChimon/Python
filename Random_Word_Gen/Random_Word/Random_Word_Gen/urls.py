from django.conf.urls import url, include

urlpatterns =[
    url(r'^', include('apps.Random_Word_Gen_App.urls')),
]
