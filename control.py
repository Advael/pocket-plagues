from random import choice

class trained:
  pass

class dumb:
  def __call__(self, moves):
    return choice(moves)

keys = {
  "Trained":trained,
  "Dumb":dumb,
  }
