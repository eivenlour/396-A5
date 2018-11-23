#CMPUT 396 ASSIGNMENT 5 
#Nim class 

class Nim:

    def __init__(self, list_of_stones):
        self.game = list_of_stones 
        self.num_of_piles = len(list_of_stones)

    def print_game(self):
        print(self.game)

    def update(self, num_of_stones, pile):
        self.game[pile] = self.game[pile] - num_of_stones

