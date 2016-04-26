from django.conf.urls import include, url, patterns
from questions.views import SurveyView, SurveyResultsView


urlpatterns = [
    url(r'^(?P<pk>[-\d]+)/$', SurveyView.as_view(), name='survey-detail'),
    url(r'^(?P<pk>[-\d]+)/results/$', SurveyResultsView.as_view(), name='survey-results'),
]
