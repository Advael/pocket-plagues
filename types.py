from bitstring import Bits

def organismType(name, number):
  '''
    (16bit bitstring, 16 character string)
      -> organismType
  '''
  attr = {}
  tbit = 'uint:16=' + str(2 ** (number - 1))
  attr = {"identifier":Bits(tbit)}
  return type(name, (), attr)

t = organismType

Electric =  t("Electric", 1)
Space =     t("Space",    2)

