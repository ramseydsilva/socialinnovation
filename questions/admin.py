from django.contrib import admin
from questions.models import Question, Answer, Option

class OptionAdmin(admin.ModelAdmin):
    list_display = ('option', 'question')
    search_fields = ('option', 'question__question')
    list_filter = ('question',)

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Option,OptionAdmin)
