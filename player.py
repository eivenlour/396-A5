# CMPUT 396 Assignment 5 
# Nim player class

from functools import reduce
import operator
import random

class Player():

    def __init__(self, P):
        self.P = P

    def update(self,state):
        self.P = state

    def xorsum(self, state):
        return reduce(operator.xor, state)

    # Picks a random move
    def pick_random_move(self, state):
        random_pile_number = random.randint(1, len(state))
        random_num_stones = random.randint(0, state[random_pile_number-1])
        while random_num_stones == 0:
            random_pile_number = random.randint(1, len(state))
            random_num_stones = random.randint(0, state[random_pile_number-1])
        return [random_num_stones, random_pile_number]

    # Finds all winning moves, then return one randomly selected winning move
    # Source: https://webdocs.cs.ualberta.ca/~hayward/396/jem/nim.html
    def get_winning_move(self,state):
        winning_moves = []
        self.update(state)

        # XOR all elements of P
        total = self.xorsum(self.P)  
        
        # Check if there is no winning move
        if total == 0: 
            return self.pick_random_move(self.P)
          
        # Finds the winning moves
        for i in range(0,len(self.P)):
            # XOR
            xor_pile = total ^ self.P[i]
            if self.P[i] >= xor_pile:
                winning_moves.append([self.P[i] - xor_pile, i+1])
        
        next_move = random.choice(winning_moves)
        return next_move





