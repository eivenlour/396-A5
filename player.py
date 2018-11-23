from functools import reduce
import operator

class Player():

    def __init__(self, P):
        self.P = P

    def xorsum(self, state):
        return reduce(operator.xor, state)
    #
    def get_winning_moves(self):
          winning_moves= [] 
          total = self.xorsum(self.P)  # xor all elements of P
          if total==0:
            print(' loss')
            return
          pile_index = 0 
          #j is the number of stones in pile 
          for j in self.P:
            #i is the number of stones taken out of the pile j 
            for i in range(0, j):
              new_state = self.P
              new_state[pile_index] = j - 1 
              if self.xorsum(new_state) == True:
                winning_moves.append([i, index + 1])
            pile_index += 1 
          return winning_moves



def main():
    state = [1,2,2]
    player = Player(state)
    player.get_winning_moves()

main()
