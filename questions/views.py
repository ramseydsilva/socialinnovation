from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.shortcuts import render
from questions.models import Question, Option, Answer, Survey


class SurveyView(ListView):
    model = Question

    def get_queryset(self):
        return self.model.objects.filter(survey=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        survey = Survey.objects.filter(id=self.kwargs['pk']).first()

        for question_id, option_id in request.POST.items():
            if question_id.isdigit():
                question = Question.objects.filter(id=question_id).first()
                option = Option.objects.filter(id=option_id).first()
                if question and option:
                    answer = Answer(option=option, user=None if request.user.is_anonymous() else request.user)
                    answer.save()

        return HttpResponseRedirect("/survey/%d/results/" %(survey.id))

class SurveyResultsView(View):
    template_name = "questions/results.html"

    def get(self, request, *args, **kwargs):
        context = {
            'survey': Survey.objects.get(id=self.kwargs['pk'])
        }
        return render(request, self.template_name, context)


