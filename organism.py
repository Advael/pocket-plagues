from combatant import combatant
from simplejson import load
import control


class organism:
  def __init__(self, jsonfile, control=None):
    self.__dict__ = load(open(jsonfile))
    self.combat = combatant(self.combat)
    self.essences = self.combat.essences
    self.tactic = control or _control(self.tactic)


def _control(tactic):
  return control.keys.__dict__[tactic]()
