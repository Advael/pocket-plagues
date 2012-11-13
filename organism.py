from simplejson import load
import typeMatrix

class organism:
  typeCost = 50
  statPointLimit = 100
  movePointLimit = 100
  totalPointLimit = 1000
  moveTotalLimit = 8
  moveActiveLimit = 4
  pointExceedMessage = "Point cost exceeded"
  movesExceedMessage = "Too many moves"

  def __init__(self, jsonName):
    self._data = load(open(jsonName + ".json"))
    self.points = self.getTypes() \
                + self.getStats() \
                + self.getMoves()
    if self.points > self.totalPointLimit:
      raise ValueError(self.pointExceedMessage)
  
  def getTypes(self):
    points = 0
    hasType = False
    self.types = (self._data["types"].split(" "))
    self.typekey = typeMatrix.check(0)
    for t in self.types:
      if not hasType:
        hasType = True
      else:
        points += self.typeCost
      self.typekey |= typeMatrix.check(t)
    return points 
  
  def getStats(self):
    self.stats = self._data["stats"]
    for i in self.stats:
      if self.stats[i] > self.statPointLimit:
        raise ValueError(self.pointExceedMessage)
    points = sum([self.stats[i] for i in self.stats])
    self.stats["health"] *= 2
    self.stats["meter"] /= 2
    self.stats["evade"] /= 2
    return points

  def getMoves(self):
    points = 0
    self.moves = self._data["moves"]
    self.active = {}

    for i in self.moves:
      self.moves[i]["typekey"] = \
      typeMatrix.check(self.moves[i]["type"])

      if self.moves[i]["mode"].title() == "Attack" \
      or self.moves[i]["mode"].title()=="Special":
        cost = self.moves[i]["dmg"] + self.moves[i]["acc"]
      elif self.moves[i]["mode"].title() == "Spell":
        pass
      elif self.moves[i]["properties"]:
        pass

      if cost > self.movePointLimit:
        raise ValueError(self.pointExceedMessage)
      points += cost
      if not self.moves[i]["selected"] == 0:
        self.active[i] = self.moves[i]
      if len(self.moves) > self.moveTotalLimit \
      or len(self.active) > self.moveActiveLimit:
        raise ValueError(self.moveExceedMessage)
    return points

  def setController(self, function):
    self.control = function

  def check(self):
    pass #check for triggers and passive effects

  def act(self):
    return self.control(self.active)
