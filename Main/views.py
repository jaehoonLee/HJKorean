from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

# Create your views here.
def main_page(request):
    return render_to_response('main.html', RequestContext(request))

def korean_black_page(request):
    return render_to_response('korean_black_page.html' , RequestContext(request))