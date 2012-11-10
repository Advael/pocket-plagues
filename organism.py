from simplejson import load
import typeMatrix

class organism:
  def __init__(self, jsonName):
    self._data = load(open(jsonName + ".json"))
    self.types = (self._data["types"].split(" "))
    self.typekey = typeMatrix.check(0)
    for t in self.types:
      self.typekey |= typeMatrix.check(t)
