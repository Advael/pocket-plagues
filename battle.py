from combatant import combatant
from trainer import trainer
import control


class battle:
  def __init__(self, one, two):
    for i in [one, two]:
      if isinstance(i, trainer.trainer) == True:
        pass
      if isinstance(i, organism.organism) == True:
        pass
  def turn(self):
    self.phaseTrainers()
    self.resolve()
    if not (self.one.stats.speed == self.two.stats.speed):
      for i in sorted([self.one.active, self.two.active], key=getSpeed):
        self.phaseOrganism(i)
        self.resolve()
    else:
      for i in [self.one, self.two]:
        self.phaseOrganism(i)
      self.resolve()

  def phaseTrainers(self):
    print "Trainer phase"

  def phaseOrganism(self, organism):
    print organism.name + " phase"

  def resolve(self):
    print "Resolved"
    # do damage calculations, etc.


def getSpeed(organism):
  return organism.stats.speed
