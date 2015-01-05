from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from Main.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import simplejson

# Create your views here.
def main_page(request):
    questionsets1 = QuestionSet.objects.all().filter(type=0)
    corrects = []
    wrongs = []
    for question_set in questionsets1:
        correct = 0
        wrong = 0
        for question in question_set.question_set.all():
            if question.correct == True:
                correct = correct + 1
            else :
                wrong = wrong + 1
        corrects.append(correct)
        wrongs.append(wrong)

    questionsets2 = QuestionSet.objects.all().filter(type=1)
    corrects2 = []
    wrongs2 = []
    for question_set in questionsets2:
        correct = 0
        wrong = 0
        for question in question_set.question_set.all():
            if question.correct == True:
                correct = correct + 1
            else :
                wrong = wrong + 1
        corrects2.append(correct)
        wrongs2.append(wrong)

    print corrects2
    print wrongs2


    return render_to_response('main.html', RequestContext(request,
                                                          {'question_sets1' : questionsets1, 'corrects' : corrects, 'wrongs' : wrongs,
                                                           'question_sets2' : questionsets2, 'corrects2' : corrects2, 'wrongs2' : wrongs2}))

def korean_black_page(request, set_id):
    questionset = QuestionSet.objects.filter(id=set_id)[0]
    questions = questionset.question_set.all()
    return render_to_response('korean_black_page.html', RequestContext(request, {'questions' : questions}))

def korean_black_page_wrong(request, set_id):
    questionset = QuestionSet.objects.filter(id=set_id)[0]
    questions = questionset.question_set.all().filter(correct=False)
    return render_to_response('korean_black_page.html', RequestContext(request, {'questions' : questions}))

@csrf_exempt
def check_answer(request):
    answer = request.POST['answer']
    id = request.POST['id']

    question = Question.objects.filter(id=id)[0]
    if str(question.answer-1) == answer:
        question.correct = True
        question.save()
        result = {'result' : 1, 'answer' :  str(question.answer)}
        return HttpResponse(simplejson.dumps(result), 'application/json')
    else :
        question.correct = False
        question.save()
        result = {'result' : 0, 'answer' :  str(question.answer)}
        return HttpResponse(simplejson.dumps(result), 'application/json')
