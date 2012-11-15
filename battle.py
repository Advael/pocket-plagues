from combatant import combatant
from trainer import trainer
import control

class battle:
  def __init__(self, one, two):
    self.one, self.two = combatant(one), combatant(two)
  def turn(self):
    self.phaseTrainers()
    for i in sorted([self.one, self.two], key=getSpeed):
      self.phaseOrganism(i)
    #Do trainer phase simultaneously
      #No part of trainer phase can affect any entity other than
      #their own organism EXCEPT when sampling
    #Do organism actions in descending order of speed
  def phaseTrainers(self):
    print "Trainer phase"
  def phaseOrganism(self, organism):
    print organism.name + " phase"

def getSpeed(organism):
  return organism.stats.speed
