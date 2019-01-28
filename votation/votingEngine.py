#oopsie doopsie
from votation import models
from datetime import datetime
from django.shortcuts import render

class Complex:
  def __init__(self, author, question, votinglist):
    self.author = author
    self.question = question
    self.votinglist = votinglist
    """
    example of votingList
    voting1 = {
      '1. yes': 10, # option
      '2. no': 23, # option
    }
    """

  def addoption(self, option):
    if option not in self.votinglist:
      self.votinglist[option] = 0 # new option is being created. it has a 0-counter
      return True #success return
    return False


  def extractquestion(self, num):
    counter=0
    for i in self.votinglist:
      counter+=1
      if counter == num:
        result = i.split(':')
        return result[0], result[1]
    return "0"


  def synchronizewithdatabase(self):
    #need to add id/question/votinglist into a database
    first = self.extractquestion(1)
    second = self.extractquestion(2)
    third = self.extractquestion(3)
    fourth = self.extractquestion(4)
    p = models.VotingsBase( self.author,
                            self.question, len(self.votinglist),
                            first[0], int(first[1]),
                            second[0], int(second[1]),
                            third[0], int(third[1]),
                            fourth[0], int(fourth[1]),
                            datetime.now())
    p.save()
    return True

def extractfromdb(request):
  tmp=models.VotingsBase.objects.filter(id=1).values()[0]
  print(tmp)#return the whole information about voting
  return render(request, 'login.html')


def testing(request):#test to add values to db
  ne = models.VotingsBase(authorid=1,question="Are u ready?",options=4,
                          option1="yes",option1counter=10,
                          option2="actually no",option2counter=5,
                          option3="of course",option3counter=13,
                          option4="hell yeah",option4counter=45, date=datetime.now())

  ne.save()
  return render(request, 'login.html')
