from django.conf.urls import include, url, patterns
from home.views import HomeView, ContactView, AboutView,LoginView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'login/$' , LoginView.as_view(),name='login')
]
