from combatant import combatant
from trainer import trainer
from organism import organism
import control


class battle:
  def __init__(self, one, two):
      self.one = organism(one)
      self.two = organism(two)
  def turn(self):
    self.damageBuffer = []
    self.phaseTrainers()
    self.resolve()
    orgs = sorted([self.one, self.two], key=getSpeed)
    if not (self.one.combat.stats.speed == self.two.combat.stats.speed):
      for i in [0, 1]:
        self.phaseOrganism(orgs[i], orgs[1-i])
        self.resolve()
    else:
      for i in [0, 1]:
        self.phaseOrganism(orgs[i], orgs[1-i])
      self.resolve()

  def phaseTrainers(self):
    print "Trainer phase"

  def phaseOrganism(self, org, target):
    print org.name + " phase"
    self.damageBuffer.append(org.tactic(org.combat.actives).execute(org, target))

  def resolve(self):
    while self.damageBuffer:
      org, effect = self.damageBuffer.pop()
      if type(effect) == type(int()):
        org.combat.currentHealth -= effect
      else:
        pass # properties stuff
    for i in [self.one, self.two]:
      if i.combat.currentHealth < 1:
        print i.name + "loses"

  def textdraw(self):
    # print self.log.fresh
    pass

def getSpeed(organism):
  return organism.combat.stats.speed
