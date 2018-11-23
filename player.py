from functools import reduce
import operator

class Player():

    def __init__(self, P):
        self.P = P

    def xorsum(self, state):
        return reduce(operator.xor, state)
    #
    def get_winning_moves(self):
          total = self.xorsum(self.P)  # xor all elements of P
          if total==0:
            print(' loss')
            return
          for j in self.P:
            tj = total ^ j  # xor
            if j >= tj:
              print(' win: take',j - tj,'from pile with',j)


def main():
    state = [1,2,2]
    player = Player(state)
    player.get_winning_moves()

main()
