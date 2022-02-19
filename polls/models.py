from django.db import models


from django.utils import timezone
import datetime
# Create your models here.

#Nombre del modelo en singular siempre
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




class Choice(models.Model):
    #relacion de uno a muchos 
    #models.CASCADE es cuando se borre una pregunta se borrara  sun opciones tambien...
    #choice opcion
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)#los votos van en 0 pues asi se le esta inicializando

    def __str__(self):
        return self.choice_text




