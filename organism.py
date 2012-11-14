from simplejson import load
from typeMatrix import check

typeCost = 50
statMax = 100
moveMax = 100
costMax = 1000
moveCount = 8
activeCount = 4

exceedError = "Maximum valid value exceeded"


class organism:
  points = 0

  def __init__(self, name):
    self._data = load(open(name + ".json"))
    self.types() 
    self.stats() 
    self.moves()
    del self._data
    assert self.points <= costMax, exceedError

  def types(self):
    self.types=map(check, set(self._data["types"].split(" ")))
    self.points += typeCost * max((len(self.types) - 1), 0)
  
  def stats(self):
    self.stats = self._data["stats"]
    for i in self.stats.values():
      assert i <= statMax, exceedError
      self.points += i
    self.stats["health"] *= 2
    self.stats["meter"] /= 2
    self.stats["evade"] /= 2

  def moves(self):
    points = 0
    self.moves, self.abilities = {}, {}
    for k, v in self._data["moves"].items():
      v["type"] = check(v["type"])
      if v["mode"].title() == "Attack" \
      or v["mode"].title() == "Special":
        cost = v["dmg"] + v["acc"]
      elif v["mode"].title() == "Spell":
        pass
      if v["properties"]:
        pass
      assert cost <= moveMax, exceedError
      points += cost
      if v["active"] == 1:
        self.moves[k] = v
      else:
        self.abilities[k] = v
    assert len(self.moves)+len(self.abilities) <= moveCount \
    and len(self.moves) <= activeCount, exceedError
    self.points += points

  def control(self, function):
    self.control = function

  def check(self):
    pass #check for triggers and passive effects

  def act(self):
    return self.control(self.active)
