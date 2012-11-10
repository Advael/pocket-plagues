from bitstring import Bits as bits
from simplejson import load

__data = load(open("typeMatrix.json"))

matrix = __data["matrix"]
names = __data["types"]
bitkeys = {}

for k in names:
  names[k] = {"n":names[k]}
  names[k]["bitkey"] = bits("uint:16="+str(2**names[k]["n"])) 
  names[k]["offense"] = matrix[names[k]["n"]]
  names[k]["defense"] = [a[names[k]["n"]] for a in matrix] 
  bitkeys[names[k]["bitkey"]] = {"name":k}
for k in bitkeys:
  bitkeys[k]["offense"] = names[bitkeys[k]["name"]]["offense"]
  bitkeys[k]["defense"] = names[bitkeys[k]["name"]]["defense"]

def checkType(key):
  """
    (valid type name or bitstring,
     string, int, or hex to use as bitstring)
      --> bitstring
  """
  if type(key) == type(bits()):
    return key
  elif type(key) == type(str()):
    if key.title() in names:
      return names[key.title()]["bitkey"]
    else:
      return bits(key)
  elif type(key) == type(int()):
    return bits("uint:16=" + str(key))
  elif type(key) == type(hex()):
    return bits("hex:16=" + str(key))
  else:
    raise TypeError('Expected a bitstring')
  

def matchup(offense, defense):
  """
    (offensive type bitstring, defensive type(s) bitstring)
      --> (numerator, denominator) for damage
  """
  num = 1
  denom = 1
  offense = checkType(offense)
  defense = checkType(defense)[::-1]
  for i in range(0, 16):
    if defense[i]:
      num *= bitkeys[offense]["offense"][i]
      denom *= 2
  return (num, denom)
