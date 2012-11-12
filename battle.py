from organism import organism

class battle:
  def __init__(self, one, two):
    #Eventually, organism vs trainer and trainer vs trainer will be handled
    if  type(one) == type(organism) \
    and type(two) == type(organism):
      pass
  def turn(self):
    #Get input
    #Do trainer actions simultaneously
    #Do organism actions in descending order of speed
