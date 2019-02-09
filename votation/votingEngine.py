# oopsie doopsie
from datetime import datetime
from votation import models
from django.shortcuts import render
import random

from votation import models


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


def extractfromdb(request, idtoextract): #extraction from db by a request and i to extract
  tmp=models.VotingsBase.objects.filter(id=idtoextract).values()[0]
  #print(tmp)  # return the whole information about voting
  return render(request, 'login.html')

def percent(num1, num2): #percent calculations
  num1 = float(num1)
  num2 = float(num2)
  percentage = '{0:.1f}'.format((num1 / num2 * 100))
  return percentage

def calculate_the_percentage(d): #making a list of % for each option
  counter=0
  ss=0
  result=[]
  for num in d:
    counter += 1
    ss += int(num)
  if ss == 0:
    return [0]*len(d)

  percsum = 0
  for num in d:
    percsum += float(percent(num, ss))
    result.append(percent(num, ss))

  # making the final sum be 100
  result[0] = '{0:.1f}'.format(float(result[0]) + float((100.0-percsum)))





  return result

def new_friendly_extract_for_profile(authorid):
  dataextr = {}
  dataextr["votes_history"] = []

  dat = models.VotingsBase.objects.filter(authorid=authorid).values_list()
  query = {}
  perc=()
  for object in dat:
    ##################
    if object[3] == 4:
      perc = (calculate_the_percentage([object[5], object[7], object[9], object[11]]))
      vars={
        object[4]: perc[0],
        object[6]: perc[1],
        object[8]: perc[2],
        object[10]: perc[3]
            }
      query = {
        'id': object[0],
        'maintitle': object[2],
        'variants': vars
        }
      #####################
    if object[3] == 3:
      perc = (calculate_the_percentage([object[5], object[7], object[9]]))
      vars={
        object[4]: perc[0],
        object[6]: perc[1],
        object[8]: perc[2]
            }
      query = {
        'id': object[0],
        'maintitle': object[2],
        'variants': vars
        }
      ####################
    if object[3] == 2:
      perc = (calculate_the_percentage([object[5], object[7]]))
      vars={
        object[4]: perc[0],
        object[6]: perc[1]
            }
      query = {
        'id': object[0],
        'maintitle': object[2],
        'variants': vars
        }

    dataextr['votes_history'].append(query)
  return dataextr

def new_friendly_extract_for_everyone():
  dataextr = {}
  dataextr["votes_history"] = []

  dat = models.VotingsBase.objects.all().values_list()
  query = {}
  perc = ()
  for object in dat:
    #####################
    if object[3] == 4:
      perc = (calculate_the_percentage([object[5], object[7], object[9], object[11]]))
      vars = {
        object[4]: perc[0],
        object[6]: perc[1],
        object[8]: perc[2],
        object[10]: perc[3]
      }
      query = {
        'id': object[0],
        'maintitle': object[2],
        'variants': vars
      }
      #####################
    if object[3] == 3:
      perc = (calculate_the_percentage([object[5], object[7], object[9]]))
      vars = {
        object[4]: perc[0],
        object[6]: perc[1],
        object[8]: perc[2]
      }
      query = {
        'id': object[0],
        'maintitle': object[2],
        'variants': vars
      }
      ####################
    if object[3] == 2:
      perc = (calculate_the_percentage([object[5], object[7]]))
      vars = {
        object[4]: perc[0],
        object[6]: perc[1]
      }
      query = {
        'id': object[0],
        'maintitle': object[2],
        'variants': vars
      }

    dataextr['votes_history'].append(query)
  return dataextr

def friendly_extract_for_everyone():  # extract all the user's history for views.py
  dataextr = {}
  dataextr["votes_history"] = []

  dat = models.VotingsBase.objects.all().values_list()
  query = []
  # creating a dict of history
  for object in dat:
    if object[3] == 4:
      perc = (calculate_the_percentage([object[5], object[7], object[9], object[11]]))
      query = [
        {'id': object[0]},
        {'maintitle': object[2]},
        {'title': object[4], 'percentage': perc[0]},
        {'title': object[6], 'percentage': perc[1]},
        {'title': object[8], 'percentage': perc[2]},
        {'title': object[10], 'percentage': perc[3]}]
    if object[3] == 3:
      perc = (calculate_the_percentage([object[5], object[7], object[9]]))
      query = [
                {'id': object[0]},
                {'maintitle': object[2]},
               {'title': object[4], 'percentage': perc[0]},
               {'title': object[6], 'percentage': perc[1]},
               {'title': object[8], 'percentage': perc[2]}]
    if object[3] == 2:
      perc = (calculate_the_percentage([object[5], object[7]]))
      query = [
        {'id': object[0]},
        {'maintitle': object[2]},
        {'title': object[4], 'percentage': perc[0]},
        {'title': object[6], 'percentage': perc[1]}]

    dataextr['votes_history'].append(query)
  return dataextr

def friendly_extract_for_profile(authorid): #extract all the user's history for views.py
  dataextr = {}
  dataextr["votes_history"] = []

  dat = models.VotingsBase.objects.filter(authorid=authorid).values_list()
  query=[]
  # creating a dict of history
  for object in dat:
    print(object)
    if object[3] == 4:
      perc=(calculate_the_percentage([object[5], object[7], object[9], object[11]]))
      query = [
              {'id': object[0] },
              {'maintitle': object[2]},
              {'title': object[4], 'percentage':perc[0]},
             {'title': object[6], 'percentage': perc[1]},
             {'title': object[8], 'percentage': perc[2]},
             {'title': object[10], 'percentage': perc[3]}]
    if object[3] == 3:
      perc = (calculate_the_percentage([object[5], object[7], object[9]]))
      query=[
              {'id': object[0]},
              {'maintitle': object[2]},
              {'title': object[4], 'percentage':perc[0]},
             {'title': object[6], 'percentage': perc[1]},
             {'title': object[8], 'percentage': perc[2]}]
    if object[3] == 2:
      perc = (calculate_the_percentage([object[5], object[7]]))
      query=[
            {'id': object[0]},
            {'maintitle': object[2]},
            {'title': object[4], 'percentage':perc[0]},
             {'title': object[6], 'percentage': perc[1]}]


    dataextr['votes_history'].append(query)


  return dataextr



def testing(request):  # test to add values to db
  ne = models.VotingsBase(authorid=1, question="working?",options=4,
                          option1=str(random.randint(1,9999999)),option1counter=10,
                          option2=str(random.randint(1,9999999)), option2counter=5,
                          option3=str(random.randint(1,9999999)), option3counter=13,
                          option4=str(random.randint(1,9999999)), option4counter=45, date=datetime.now())

  ne.save()

  return render(request, 'login.html')

def addvoting(request): #func to add voting to db
  votingfielddata = request.POST
  userids = request.user.id
  vars=[]

  for i in range(1, 5):
    if votingfielddata['var'+str(i)] != "":
      vars.append(votingfielddata['var'+str(i)])
  numofvars = len(vars)

  # kostil activated (c) Semen

  try:
    vars.remove('')
  except ValueError:
    pass
  try:
    vars.remove('')
  except ValueError:
    pass
  try:
    vars.remove('')
  except ValueError:
    pass

  vars.append("")
  vars.append("")
  vars.append("")
  vars.append("")

  # noone will crash server by leaving blank lines :D

  ne = models.VotingsBase(authorid=userids, question=votingfielddata['title'], options=numofvars,
                          option1=vars[0], option1counter=0,
                          option2=vars[1], option2counter=0,
                          option3= vars[2], option3counter=0,
                          option4=vars[3], option4counter=0, date=datetime.now())
  ne.save()

  return render(request, 'profile.html')
