from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from Main.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import simplejson

# Create your views here.
def main_page(request):
    return render_to_response('main.html', RequestContext(request))

def korean_black_page(request):
    questions = Question.objects.all()
    return render_to_response('korean_black_page.html', RequestContext(request, {'questions' : questions}))

@csrf_exempt
def check_answer(request):
    answer = request.POST['answer']
    id = request.POST['id']

    question = Question.objects.filter(id=id)[0]
    if str(question.answer-1) == answer:
        result = {'result' : 1, 'answer' :  str(question.answer)}
        return HttpResponse(simplejson.dumps(result), 'application/json')
    else :
        result = {'result' : 0, 'answer' :  str(question.answer)}
        return HttpResponse(simplejson.dumps(result), 'application/json')
