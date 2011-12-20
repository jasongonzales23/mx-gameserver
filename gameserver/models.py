from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=50) 
    teamID=models.CharField(max_length=255) #this will be generated on the iPad
    checkIn=models.DateTimeField(default=datetime.now())
    #score=models.IntegerField(max_length=6) #may not need this, can just calculate based on answer model
    
    def __unicode__(self):
        return self.name

class Player(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255, blank=True)
    team=models.ForeignKey(Team)
    
    def __unicode__(self):
        return self.name
    
#dont't need this    
#class Question(models.Model):
#    number=models.CharField(max_length=10)
#    correctAnswer=models.TextField(max_length=255)#need to make this optional and allow for non textual answers?
#    possiblePoints=models.IntegerField(max_length=5)
#    
#    def __unicode__(self):
#        return self.number
    
class Answer(models.Model):
    team=models.ForeignKey(Team)
    question=models.IntegerField(max_length=5)
    answerGiven=models.TextField(max_length=255)
    pointsAwarded=models.CharField(max_length=5)
    
    def __unicode__(self):
        return self.answerGiven
    
    