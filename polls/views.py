from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('hello world')

def detail(request, question_id):
    return HttpResponse('hello detail' + str(question_id))

def result(request, question_id):
    return HttpResponse('hello result' + str(question_id))