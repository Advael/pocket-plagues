from simplejson import load
from fuzzywuzzy import process
from fractions import Fraction

__data = load(open("typeMatrix.json"))
matrix = __data["matrix"]
names = __data["types"]
del __data

def check(orgType):
  r = process.extractOne(orgType, names)
  assert r[1] > 90, "Ambiguous or invalid type."
  return r[0]

def matchup(offense, defense):
  """
  (string, list of string) -> Fraction
  """
  n = 1
  d = 1
  o = matrix[names.index(check(offense))]
  for i in defense:
    n *= o[names.index(check(i))]
    d *= 2
  return Fraction(n, d)
