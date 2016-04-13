from django.views.generic import TemplateView
from questions.models import Question


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['greeting'] = "Welcome!"
        context['questions'] = Question.objects.all()
        return context