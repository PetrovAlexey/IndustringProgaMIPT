from django.db import models

from django.db import models
from django.urls import reverse

from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse('polls:question', kwargs={'pk': self.pk})

    def answers(self):
        return self.answer_set.order_by('id')
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('polls:question', kwargs={'pk': self.question_id})

    def __str__(self):
        return self.text

    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
