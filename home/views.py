from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from questions.models import Question, Survey, Contact


class HomeView(ListView):
    model = Survey
    template_name = "home/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['greeting'] = "Welcome!"
        return context

class ContactView(TemplateView):
    template_name = "home/contact.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        error = ''
        success=False
        name = self.request.POST.get("name", "")
        email = self.request.POST.get("email", "")
        message = self.request.POST.get("message", "")

        print name, email, message

        if not name:
            error = "You need to enter a name"
        elif not email:
            error = "You need to enter a valid email address"
        elif not message:
            error = "You need to enter your message"
        else:
            contact=Contact(name=name,email=email,message=message)
            contact.save()
            success=True

        context = {
            'error': error,
            'success': success,
            'name': name,
            'email': email,
            'message': message,
        }

        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name ="home/about.html"

class RegisterView(View):
    template_name ="registration/register.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        error = ''
        name = self.request.POST.get("name", "")
        email = self.request.POST.get("email", "")
        phone = self.request.POST.get("phone", "")
        password1 = self.request.POST.get("password1", "")
        password2 = self.request.POST.get("password2", "")
        agree = bool(self.request.POST.get("agree", False))

        if not name:
            error = "You need to enter a name"
        elif not email:
            error = "You need to enter a valid email address"
        elif not phone:
            error = "You need to enter your phone number"
        elif not password1:
            error = "You need to enter a password"
        elif not password2:
            error = "You need to confirm your password"
        elif password1 != password2:
            error = "Passwords don't match"
        elif not agree:
            error = "You need to agree to terms and conditions"
        elif User.objects.filter(username=email).exists():
            error = "This user has already been registered"
        else:
            user = User.objects.create_user(email, email, password1, first_name=name)
            user = authenticate(username=email, password=password1)
            if user:
                return HttpResponseRedirect("/")
            else:
                error = "Problem authenticating user"

        context = {
            'error': error,
            'name': name,
            'email': email,
            'phone': phone,
            'password1': password1,
            'password2': password2,
            'agree': agree
        }

        return render(request, self.template_name, context)

