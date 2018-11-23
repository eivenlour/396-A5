from functools import reduce
import operator

class Player():

    def __init__(self, list_piles):
        self.list_piles = list_piles
        self.possible_moves = []

    def xorsum(state):
        return reduce(operator.xor(), state)
    #
    # def get_winning_moves():
    #       total = xorsum(P)  # xor all elements of P
    #       if total==0:
    #         print(' loss')
    #         return
    #       for j in P:
    #         tj = total ^ j  # xor
    #         if j >= tj:
    #           print(' win: take',j - tj,'from pile with',j)


def main():
    state = [1,2,3]
    player = Player(state)
    print(player.xorsum())

main()
