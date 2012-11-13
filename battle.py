from organism import organism
import control

class battle:
  def __init__(self, one, two):
    for i in [one, two]:
      if type(i) == type(organism):
        i.setController(control.dumb)
      elif type(i) == type(trainer):
        i.setController(control.basicPlayer)
  def turn(self):
    pass

    #Do trainer actions simultaneously
    #Do organism actions in descending order of speed
