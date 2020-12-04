from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# Create your models here.
class Quiz(models.Model):
    id = models.CharField(primary_key=True,max_length=100, unique=True)
    judul = models.CharField(max_length=1000)
    class Meta:
        #ordering = ['created',]
        #verbose_name_plural ="Quizzes"
        def __str__(self):
            return self.judul

class Questions(models.Model):
    id = models.CharField(primary_key=True,max_length=100, unique=True)
    text = models.CharField(max_length=1000)
    corrans=models.CharField(max_length=100)
    c1=models.CharField(max_length=100)
    c2=models.CharField(max_length=100)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Answer(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    username=models.CharField(max_length=1000, unique=True)
    answer=models.CharField(max_length=100)
    """ abaikan ini
        SELECT count(*) 
        FROM Questions 
        INNER JOIN Quiz on Quiz.id=Questions.quiz_id
        WHERE question_id=Questions.id and answer=Questions.corrans;
    """
    def __str__ (self):
        return self.answer

