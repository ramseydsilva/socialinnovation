from django.conf.urls import include, url, patterns
from questions.views import QuestionView


urlpatterns = [
    url(r'^(?P<pk>[-\d]+)/$', QuestionView.as_view(), name='question-detail'),
]
