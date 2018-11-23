from Nim import Nim

def main():
    # Get player input
    init_input_string = input("Enter the list of number of stones you want in each pile, separated by a space character. (Example: 2 3 5)\n")
    init_input_list = convert_input(init_input_string)

    # Check if initial input contains a pile with 0 stones
    while not init_input_is_valid(init_input_list):
        init_input_string = input("Invalid input. Try again.\n")
        init_input_list = convert_input(init_input_string)

    # Initialize Nim class
    nim = Nim(init_input_list)


    # Check if game is not over
    while not nim.check_end_game():
        input_string = input("Enter the number of stones you want to take and the pile you want the stones taken from.\nNote that the pile numbering starts from 0.\n Example: 2 0 - means 2 stones will be taken from the first pile.")
        input_list = convert_input(input_string)
        num_stones = input_list[0]
        pile = input_list[1]
        nim.update(num_stones, pile)


def init_input_is_valid(input_list):
    for each_item in input_list:
        if each_item == 0:
            return False
    return True

def convert_input(input_string):
    input_string = input_string.split()
    input_list = []
    for each_item in input_string:
        input_list.append(int(each_item))
    return input_list

main()