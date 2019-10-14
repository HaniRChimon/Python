from django.conf.urls import url, include

urlpatterns = [
 url(r'^', include('apps.nin_gold.urls')),
]