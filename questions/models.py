from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=500)

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
    option = models.ForeignKey(Option)
    date = models.DateTimeField(auto_now_add=True)
