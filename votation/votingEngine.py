# oopsie doopsie
from datetime import datetime
from votation import models
from django.shortcuts import render
import random
class Complex:
  def __init__(self, authorsid, question, options,
                          option1=None ,option1counter=None,
                          option2=None,option2counter=None,
                          option3=None,option3counter=None,
                          option4=None,option4counter=None, date=None):
    self.authorsid = authorsid
    self.question = question
    self.options = options

    self.option1 = option1 if option1 is not None else ""
    self.option1counter = option1counter if option1counter is not None else 0

    self.option2 = option2 if option2 is not None else ""
    self.option2counter = option2counter if option2counter is not None else 0

    self.option3 = option3 if option3 is not None else ""
    self.option3counter = option3counter if option3counter is not None else 0

    self.option4 = option4 if option4 is not None else ""
    self.option4counter = option4counter if option4counter is not None else 0

    self.date = datetime.date(date) if date is not None else datetime.now()  #datetime.date(2018, 13, 14)

  def addoption(self, optionid, optionstring, optioncounter): #func to change or add question and its counter
    if optionid == 1:
      self.option1 = optionstring
      self.option1counter = int(optioncounter)
    elif optionid == 2:
      self.option2 = optionstring
      self.option2counter = int(optioncounter)
    elif optionid == 3:
      self.option3 = optionstring
      self.option3counter = int(optioncounter)
    elif optionid == 4:
      self.option4 = optionstring
      self.option4counter = int(optioncounter)
    return self

  def synchronizewithdatabase(self): # func to add object to db

    p = models.VotingsBase( self.author,
                            self.question, self.options,
                            self.option1, int(self.option1counter),
                            self.option2, int(self.option2counter),
                            self.option3, int(self.option3counter),
                            self.option4, int(self.option4counter),
                            self.date)
    p.save()
    return self


def extractfromdb(request, idtoextract): #extraction from db
  tmp=models.VotingsBase.objects.filter(id=idtoextract).values()[0]
  print(tmp)  # return the whole information about voting
  return render(request, 'login.html')




def calculate_the_percentage(d):
  counter=0
  ss=0
  result=[]
  for num in d:
    counter += 1
    ss += int(num)

  for num in d:
    tmp= (num/ss)*100
    tmp = int(tmp)
    result.append(tmp)

  for num in result:
    if sum(result)<100:
      result[0]+=1

  return result

def friendly_extract_for_profile(authorid): #extract all the user history for views.py
  dataextr = {}
  dataextr["votes_history"] = []

  dat = models.VotingsBase.objects.filter(authorid=authorid).values_list()
  query=[]
  for object in dat:
    if object[3] == 4:
      perc=(calculate_the_percentage([object[3], object[5], object[7], object[9]]))
      query = [{'title': object[4], 'percentage':perc[0]},
             {'title': object[6], 'percentage': perc[1]},
             {'title': object[8], 'percentage': perc[2]},
             {'title': object[10], 'percentage': perc[3]}]
    if object[3] == 3:
      query=[{'title': object[4], 'percentage':object[3]},
             {'title': object[6], 'percentage': object[5]},
             {'title': object[8], 'percentage': object[7]}]
    if object[3] == 2:
      query=[{'title': object[4], 'percentage':object[3]},
             {'title': object[6], 'percentage': object[5]}]


    dataextr['votes_history'].append(query)


  return dataextr


def testing(request):  # test to add values to db
  ne = models.VotingsBase(authorid=1, question="ARE YOU GAY?",options=4,
                          option1=str(random.randint(1,9999999)),option1counter=10,
                          option2=str(random.randint(1,9999999)), option2counter=5,
                          option3=str(random.randint(1,9999999)), option3counter=13,
                          option4=str(random.randint(1,9999999)), option4counter=45, date=datetime.now())

  ne.save()
  return render(request, 'login.html')

