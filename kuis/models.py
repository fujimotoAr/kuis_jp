from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Quiz(models.Model):
    id = models.CharField(primary_key=True,max_length=100, unique=True)
    judul = models.CharField(max_length=1000)
    class Meta:
        def __str__(self):
            return self.judul

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000)
    corrans=models.CharField(max_length=100)
    c1=models.CharField(max_length=100)
    c2=models.CharField(max_length=100)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Answer(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    username=models.CharField(max_length=1000, unique=True)
    score=models.IntegerField(default=0)
    def __str__ (self):
        return self.answer

