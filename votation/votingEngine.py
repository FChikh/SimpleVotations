#oopsie doopsie

class Complex:
  def __init__(self, id, question, votinglist):
    self.id = id
    self.question = question
    self.votinglist = votinglist
    """
    example of votingList
    voting1 = {
      '1. yes': 10, # option
      '2. no': 23, # option
    }
    """

  def AddOption(self, option):
    if option not in self.votinglist:
      self.votinglist[option] = 0 # new option is being created. it has a 0-counter
      return True #success return
    return False

  def synchronizeWithDatabase(self):
    #need to add id/question/votinglist into a database
    pass
