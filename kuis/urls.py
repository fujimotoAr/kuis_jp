from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soal/', views.question, name='question'),
    path('ans/', views.answer, name='answer'),
]