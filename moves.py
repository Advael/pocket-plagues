from fuzzywuzzy import process, fuzz
from essences import check
from errors import ExceedError

moveMax = 100
moveCount = 8
activeCount = 4



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
    assert self._p <= moveMax, ExceedError
    self._p = max(self._p, 0)
