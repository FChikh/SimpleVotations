from django.db import models

# Create your models here.

class VotingsBase(models.Model):
  id = models.IntegerField()
  author = models.CharField(max_length=20)
  question = models.CharField(max_length=144)
  options = models.IntegerField()
  option1 = models.CharField(max_length=50)
  option2 = models.CharField(max_length=50)
  option3 = models.CharField(max_length=50)
  option4 = models.CharField(max_length=50)
  date = models.DateTimeField()