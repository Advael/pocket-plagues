from simplejson import load
from fuzzywuzzy import process
from fractions import Fraction

__data = load(open("typeMatrix.json"))
matrix = __data["matrix"]
types = __data["types"]
del __data

def check(orgType):
  r = process.extractOne(orgType, types)
  assert r[1] > 90, "Ambiguous or invalid type."
  return r[0]

def matchup(offense, defense):
  n = 1
  d = 1
  o = matrix[types[check(offense)]]
  for i in defense:
    n *= o[types[check(i)]]
    d *= 2
  return Fraction(n, d)
