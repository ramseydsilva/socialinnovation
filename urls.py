from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^survey/', include('questions.urls', namespace="questions")),
    url(r'', include('home.urls', namespace="home")),
]
