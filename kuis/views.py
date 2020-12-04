from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Quiz,Questions,Answer
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

def index(request):
    quiz_list=Quiz.objects.order_by('id')
    quiz_data=serializers.serialize('json', quiz_list, fields=('id','judul'))
    return HttpResponse(quiz_data)




def question(request):
    question_list=get_list_or_404(Questions,quiz_id=request.GET.get('id'))
    question_data=serializers.serialize('json', question_list, fields=('id','text','c1','c2'))
    return HttpResponse(question_data)
"""
def question(request,quiz_id):
    #question_list=Questions.objects.order_by('id')
    question_list=get_list_or_404(Questions,quiz_id=quiz_id)
    question_data=serializers.serialize('json', question_list, fields=('id','text','c1','c2'))
    #return render(request,'kuis/questions.html',{'question_list':question_list})
    return HttpResponse(question_data)

"""