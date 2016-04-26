from django.contrib import admin
from questions.models import Question, Answer, Option, Survey

class OptionAdmin(admin.ModelAdmin):
    list_display = ('option', 'question')
    search_fields = ('option', 'question__question')
    list_filter = ('question',)

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question', 'survey')
    search_fields =('question',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('option', 'question', 'user', 'date')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Option,OptionAdmin)
admin.site.register(Survey)
