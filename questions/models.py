from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=500)
    survey = models.ForeignKey('Survey', related_name="questions")

    def __unicode__(self):
        return self.question

    def get_absolute_url(self):
        return '/questions/%d' %(self.id)

class Option(models.Model):
    option = models.CharField(max_length=500)
    question = models.ForeignKey(Question, related_name="options")

    def __unicode__(self):
        return self.option

class Answer(models.Model):
    option = models.ForeignKey(Option, related_name="answers")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', null=True, blank=True)

    def __unicode__(self):
        return self.option.option

    @property
    def question(self):
        return self.option.question

class Survey(models.Model):
    title=models.CharField(max_length=500)
    publish_date=models.DateField(auto_now_add=True)
    open=models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/survey/%d" %(self.id)

class Contact(models.Model):
      email=models.CharField(max_length=500)
      name=models.CharField(max_length=200)
      message=models.TextField()

