from django.contrib import admin

from .models import Answer, Questions, Quizz, Result

# Register your models here.

class AnswerInLine(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answer)

admin.site.register(Result)
admin.site.register(Quizz)