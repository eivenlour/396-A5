#CMPUT 396 ASSIGNMENT 5 
#Nim class 

class Nim:

    def __init__(self, list_of_stones):
        self.game = list_of_stones 
        self.num_of_piles = len(list_of_stones)

    def print_game(self):

        print(' '.join(map(str,self.game)))

    def update(self, num_of_stones, pile):
        self.game[pile] = self.game[pile] - num_of_stones
        self.print_game()

    def check_end_game(self):
    	for item in self.game:
    		if item != 0:
    			return False 
    	return True 

