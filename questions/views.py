from django.views.generic.detail import DetailView
from questions.models import Question


class QuestionView(DetailView):
    model = Question
