
# Valores de las cartas
#   1 espadas   = 14
#   1 basto     = 13
#   7 espadas   = 12
#   7 oro       = 11
#   3,3,3,3     = 10
#   2,2,2,2     = 9
#   1 oro/copa  = 8
#   12,12,12,12 = 7
#   11,11,11,11 = 6
#   10,10,10,10 = 5
#   7 copa/basto= 4
#   6,6,6,6     = 3
#   5,5,5,5     = 2
#   4,4,4,4     = 1 

import random
class Truco:
   def barajar(self):
      """
       Baraja el mazo completo.
      """
      random.shuffle(self.cartas)
   
   def repartir(self):
      players = self._kargs['n_players']
      pass

   def __init__(self, **kargs):

        self._kargs = kargs
        self.cartas = [
            {'name': 'ancho de espadas', 'value': 14},
            {'name': 'dos de espadas', 'value': 9},
            {'name': 'tres de espadas', 'value': 10},
            {'name': 'cuatro de espadas', 'value': 1},
            {'name': 'cinco de espadas', 'value': 2},
            {'name': 'seis de espadas', 'value': 3},
            {'name': 'siete de espadas', 'value': 12},
            {'name': 'diez de espadas', 'value': 5},
            {'name': 'once de espadas', 'value': 6},
            {'name': 'doce de espadas', 'value': 7},

            {'name': 'ancho de oro', 'value': 8},
            {'name': 'dos de oro', 'value': 9},
            {'name': 'tres de oro', 'value': 10},
            {'name': 'cuatro de oro', 'value': 1},
            {'name': 'cinco de oro', 'value': 2},
            {'name': 'seis de oro', 'value': 3},
            {'name': 'siete de oro', 'value': 11},
            {'name': 'diez de oro', 'value': 5},
            {'name': 'once de oro', 'value': 6},
            {'name': 'doce de oro', 'value': 7},

            {'name': 'ancho de basto', 'value': 13},
            {'name': 'dos de basto', 'value': 9},
            {'name': 'tres de basto', 'value': 10},
            {'name': 'cuatro de basto', 'value': 1},
            {'name': 'cinco de basto', 'value': 2},
            {'name': 'seis de basto', 'value': 3},
            {'name': 'siete de basto', 'value': 4},
            {'name': 'diez de basto', 'value': 5},
            {'name': 'once de basto', 'value': 6},
            {'name': 'doce de basto', 'value': 7},

            {'name': 'ancho de copas', 'value': 8},
            {'name': 'dos de copas', 'value': 9},
            {'name': 'tres de copas', 'value': 10},
            {'name': 'cuatro de copas', 'value': 1},
            {'name': 'cinco de copas', 'value': 2},
            {'name': 'seis de copas', 'value': 3},
            {'name': 'siete de copas', 'value': 4},
            {'name': 'diez de copas', 'value': 5},
            {'name': 'once de copas', 'value': 6},
            {'name': 'doce de copas', 'value': 7},
        ]
