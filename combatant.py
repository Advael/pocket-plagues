from simplejson import load
from essences import check
from moves import _move
from errors import ExceedError

typeCost = 50
statMax = 100
costMax = 1000

class combatant:
  def __init__(self, jsonfile):
    self.__dict__ = dict(self.__dict__.items() + load(open(jsonfile)).items())
    self.types, self.points = _types(self.types)
    self.stats = _stats(self.stats)
    self.moves = [_move(m) for m in self.moves.items()]
    self.actives = [m for m in self.moves if m.active == 1]
    self.points += self.stats._p + sum([m._p for m in self.moves])
    assert self.points <= costMax, ExceedError


def _types(types):
    t = set(map(check, types.split(" ")))
    p = typeCost * max(len(t), 0)
    return t, p


class _stats:
  def __init__(self, stats):
    stats["_p"] = 0
    for i in stats.values():
      assert i <= statMax, ExceedError
      stats["_p"] += i
    self.__dict__ = stats
    self.health *= 2
    self.meter /= 2
    self.evade /= 2
