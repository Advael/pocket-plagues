from fuzzywuzzy import process, fuzz
from essences import check
from errors import ExceedError
from rules import *
from essences import matchup
from fractions import Fraction


class _move:
  def __init__(self, moveTuple):
    self.__dict__ = moveTuple[1]
    self.name = moveTuple[0]
    if fuzz.ratio(self.mode, "Trainer") > 90:
      pass
    else:
      if self.mode in ["Attack", "Special"]:
        self._p = self.damage + self.accuracy
        self.essence = check(self.essence)
      elif fuzz.ratio(self.mode, "Spell") > 90:
        pass
      if self.properties:
        pass
    assert self._p <= moveMax, ExceedError
    self._p = max(self._p, 0)

  def execute(self, user, target):
    if self.mode in ["Attack", "Special"]:
      if self.accuracy > target.stats.evade:
        result = self.damage
        result *= matchup(self.essence, target.essences)
        if self.essence in user.essences:
          result *= Fraction(3/2)
        if self.mode == "Attack":
          result *= user.stats.attack / target.stats.defense
        elif self.mode == "Special":
          result *= user.stats.special ** 2 / target.stats.resist ** 2
        return int(result)
      else:
        return "Miss"
    elif self.mode == "Spell":
      pass
