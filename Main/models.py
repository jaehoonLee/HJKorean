from django.db import models
from django.contrib import admin

class QuestionSetManager(models.Manager):
    def create_question_set(self, name, type, set_num):
        question_set = self.model(name=name, type=type, set_num=set_num)
        question_set.save()

class QuestionSet(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    set_num = models.IntegerField()
    objects = QuestionSetManager()

class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'set_num')

admin.site.register(QuestionSet, QuestionSetAdmin)

class QuestionManager(models.Manager):
    def create_question(self, url, answer):
        question = self.model(url=url, answer=answer)
        question.save()
        return question

class Question(models.Model):
    url = models.CharField(max_length=255)
    answer = models.IntegerField()
    correct = models.BooleanField()
    question_set = models.ForeignKey(QuestionSet)
    objects = QuestionManager()

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question_set_name',  'url', 'answer')
    def question_set_name(self, obj):
        return obj.question_set.name

admin.site.register(Question, QuestionAdmin)
