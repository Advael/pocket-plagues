from combatant import combatant
from simplejson import load
import control


class organism:
  def __init__(self, jsonfile, control=None):
    self.__dict__ = load(open(jsonfile))
    if self.combat:
      self.combat = combatant(self.combat)
    elif self.genome:
      self.combat = combatant(phenotype(self.genome))
      # do more stuff
    self.tactic = control or _control(self.tactic)



def phenotype(genome):
  """
    return the combat phenotype from IV and EV based values
  """
  pass

def _control(tactic):
  return control.keys[tactic]()
