from django.conf.urls import include, url, patterns
from home.views import HomeView, ContactView, AboutView ,RegisterView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    
]
