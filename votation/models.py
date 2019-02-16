from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class VotingsBase(models.Model):
    id = models.AutoField(primary_key=True)
    authorid = models.IntegerField()
    question = models.CharField(max_length=144)
    options = models.IntegerField()
    option1 = models.CharField(max_length=50)
    option1counter = models.IntegerField()
    option2 = models.CharField(max_length=50)
    option2counter = models.IntegerField()
    option3 = models.CharField(max_length=50)
    option3counter = models.IntegerField()
    option4 = models.CharField(max_length=50)
    option4counter = models.IntegerField()
    date = models.DateTimeField(null=True)
    multi = models.IntegerField(default=0)  # 0 is false 1 is true


class VotingHistory(models.Model):
    id = models.AutoField(primary_key=True)
    golosid = models.IntegerField()
    userid = models.IntegerField()
    date = models.DateTimeField(null=True)


class ReportsHistory(models.Model):
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100)
    answer = models.CharField(max_length=1000)
