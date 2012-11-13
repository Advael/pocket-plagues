from random import choice

def dumb(moves):
  return choice(moves)

def basicPlayer(moves):
  print "Choose a move (0<choice<5):"
  number = 1
  for i in moves:
    print str(number) + ". " + i["name"]
  choice = int(raw_input())
  if choice < 5 and choice > 0:
    return moves[choice]
