from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Quiz,Questions,Answer
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    quiz_list=Quiz.objects.order_by('id')
    quiz_data=serializers.serialize('json', quiz_list, fields=('id','judul'))
    return HttpResponse(quiz_data)

def question(request):
    question_list=get_list_or_404(Questions,quiz_id=request.GET.get('id'))
    question_data=serializers.serialize('json', question_list, fields=('id','text','c1','c2'))
    return HttpResponse(question_data)

@csrf_exempt
def answer(request):
    data = json.loads(request.body.decode('utf-8'))
    output_dictionary={ }
    hitung_true=0
    for i in range(1,6):
        s="q"+str(i)
        cur=get_list_or_404(Questions,quiz_id=data['id'])
        for j in cur:
            if int(j.id) % 5 == int(i) % 5:
                if(data[s]==j.corrans):
                    output_dictionary.update({s:"true"})
                    hitung_true+=1
                else:
                    output_dictionary.update({s:"false"})
    
    output_dictionary.update({"score":hitung_true * 20})
    
    #MASUKIN KE DATABASE
    try:
        add_database=Answer.objects.create(username=data['username'],quiz_id=data['id'],score=output_dictionary['score'])
    except IntegrityError:
        add_database=Answer.objects.update(username=data['username'],quiz_id=data['id'],score=output_dictionary['score'])

    ###
    
    return JsonResponse(output_dictionary)