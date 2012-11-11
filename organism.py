from simplejson import load
import typeMatrix




class organism:
  typeCost = 64
  def __init__(self, jsonName):
    self.points = 0
    self._data = load(open(jsonName + ".json"))
    hasType = False
    self.types = (self._data["types"].split(" "))
    self.typekey = typeMatrix.check(0)
    for t in self.types:
      if not hasType:
        hasType = True
      else:
        self.points += self.typeCost
      self.typekey |= typeMatrix.check(t)
    for s in self._data["stats"]:
      pass #do some stuff

