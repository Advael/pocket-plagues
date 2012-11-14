from organism import organism
from trainer import trainer
import control

class battle:
  def __init__(self, one, two):
    self.one, self.two = one, two
    for i in [self.one, self.two]:
      if type(i) == type(organism):
        i.setController(control.dumb)
      elif type(i) == type(trainer):
        i.setController(control.basicPlayer)
  def turn(self):
    phaseTrainers()
    

    #Do trainer phase simultaneously
      #No part of trainer phase can affect
    #Do organism actions in descending order of speed
  def phaseTrainers(self):
    pass
  def phase(self, organism):

