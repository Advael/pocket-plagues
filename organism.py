from simplejson import load
from typeMatrix import check
from fuzzywuzzy import process, fuzz

typeCost = 50
statMax = 100
moveMax = 100
costMax = 1000
moveCount = 8
activeCount = 4

exceedError = "Maximum valid value exceeded"

class organism:
  def __init__(self, name):
    self.__dict__ = dict(self.__dict__.items() + load(open(name)).items())
    self.types, self.points = self._types(self.types)
    self.stats = self._stats(self.stats)
    self.moves = [self._move(m) for m in self.moves.items()]
    self.actives = [m for m in self.moves if m.active == 1]
    self.points += self.stats._p + sum([m._p for m in self.moves])
    assert self.points <= costMax, exceedError

  def _types(self, types):
      t = set(map(check, types.split(" ")))
      p = typeCost * max(len(t), 0)
      return t, p

  class _stats:
    def __init__(self, stats):
      stats["_p"] = 0
      for i in stats.values():
        assert i <= statMax, exceedError
        stats["_p"] += i
      self.__dict__ = stats
      self.health *= 2
      self.meter /= 2
      self.evade /= 2

  class _move:
    def __init__(self, moveTuple):
      self.__dict__ = moveTuple[1]
      self.name = moveTuple[0]
      self.type = check(self.type)
      if process.extract(self.mode, ["Attack", "Special"])[1] > 90:
        self._p = self.dmg + self.acc
      elif fuzz.ratio(self.mode, "Spell") > 90:
        pass
      if self.properties:
        pass
      assert self._p <= moveMax, exceedError
      self._p = max(self._p, 0)

  def control(self, function):
    self.control = function

  def check(self):
    pass #check for triggers and passive effects

  def act(self):
    return self.control(self.actives)
