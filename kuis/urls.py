from django.urls import path

from . import views

urlpatterns = [
    # /quizzes/
    path('', views.index, name='index'),
    # /quizzes/2/
    #path('<str:quiz_id>/', views.question, name='question'),
    path('soal/', views.question, name='question'),
]