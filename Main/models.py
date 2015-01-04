from django.db import models
from django.contrib import admin

# Create your models here.
class QuestionManager(models.Manager):
    def create_question(self, url, answer):
        question = self.model(url=url, answer=answer)
        question.save()
        return question

class Question(models.Model):
    url = models.CharField(max_length=255)
    answer = models.IntegerField()
    objects = QuestionManager()

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'answer')

admin.site.register(Question, QuestionAdmin)

