from functools import reduce
import operator
import random

class Player():

    def __init__(self, P):
        self.P = P
        self.winning_moves = [] 

    def update(self,state):
        self.P = state

    def xorsum(self, state):
        return reduce(operator.xor, state)

    def pick_random_move(self, state):
        random_pile_number = random.randint(1, len(state))
        random_num_stones = random.randint(0, state[random_pile_number-1])
        while random_num_stones == 0:
            random_pile_number = random.randint(1, len(state))
            random_num_stones = random.randint(0, state[random_pile_number-1])
        return [random_num_stones, random_pile_number]

    #finds all winning move first, then return one randomly selected winning move
    def get_winning_move(self,state):
          self.update(state)
          total = self.xorsum(self.P)  # xor all elements of P
          if total==0: 
            #print("There is no winning move for the computer player.")
            return self.pick_random_move(self.P)
          pile_index = 0 

          non_zero_pile = []
          #if there is only one pile left, winning move is to take all of the stones 
          for i in self.P:
            if i != 0:
              non_zero_pile.append(i)
          if len(non_zero_pile) == 1:
              print(non_zero_pile)
              return [non_zero_pile[0],self.P.index(non_zero_pile[0])+1]
          #for j in self.P:
          #j is the number of stones in pile
          for j in self.P:
            #i is the number of stones taken out of the pile j 
            for i in range(1, j+1):
              new_state = self.P[:]
              new_state[pile_index] = j - i
              #if there is no stone left after the move, winning move
              if sum(new_state) == 0: 
                self.winning_moves.append([i, pile_index])
              elif self.xorsum(new_state) != 0:
                self.winning_moves.append([i, pile_index])
            pile_index += 1 

          move = random.choice(self.winning_moves)
          return move

          # tj = total ^ j  # xor
          #   if j >= tj:
          #     winning_moves.append([j-tj, pile_index])
          #   pile_index += 1 
          # return winning_move





