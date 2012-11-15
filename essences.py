from simplejson import load
from fuzzywuzzy import process
from fractions import Fraction
from errors import EssenceError


class essences:
  def __init__(self):
    self.__dict__ = load(open("essences.json"))

essences = essences()


def check(essence):
  r = process.extractOne(essence, essences.names)
  assert r[1] > 90, EssenceError
  return r[0]


def matchup(offense, defense):
  n = 1
  d = 1
  o = essences.matrix[essences.names[check(offense)]]
  if type(defense) == type(str()):
    defense = defense.split(" ")
  for i in defense:
    n *= o[essences.names[check(i)]]
    d *= 2
  return Fraction(n, d)
