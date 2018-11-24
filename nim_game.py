from Nim import Nim

def main():
    # Get player input
    init_input_string = input("Enter the list of number of stones you want in each pile, separated by a space character. (Example: 2 3 5)\n")
   
    # Check if initial input is valid
    while not init_input_is_valid(init_input_string)[0]:
        init_input_string = input("Invalid input. Try again.\n")
    init_input_list = init_input_is_valid(init_input_string)[1]
    print(init_input_list)

    # Initialize Nim class
    nim = Nim(init_input_list)

    # Check if game is not over
    while not nim.check_end_game():
        input_string = input("Enter the number of stones you want to take and the pile number you want the stones taken from.\nNote that the pile numbering starts from 1.\nExample: 2 1 - means 2 stones will be taken from the first pile.\n")

        # Check if input is valid
        while not input_is_valid(nim, input_string)[0]:
            input_string = input("Invalid input. Try again.\n")
        input_list = convert_input(input_string)
        num_stones = input_list[0]
        pile_number = input_list[1]   
        nim.update(num_stones, pile_number)

def init_input_is_valid(init_input_string):
    init_input_list = convert_input(init_input_string)
    converted_list = []
    for each_item in init_input_list:
        if not is_integer(each_item):
            return False, None
        # Check if the number of stones in each pile is greater than 0
        if int(each_item) == 0:
            return False, None
        converted_list.append(int(each_item))
        
    return True, converted_list

def input_is_valid(nim, input_string):
    current_state = nim.return_state()
    input_list = convert_input(input_string)
    converted_list = []

    # Check if all items are integers
    for each_item in input_list:
        if not is_integer(each_item):
            return False, None
        converted_list.append(int(each_item))
    
    # Check if input list has 2 items
    if len(input_list) != 2:
        return False, None

    # Check if the pile number does not exceed the number of piles
    if converted_list[1] > len(current_state):
        return False, None

    # Check if the number of stones to take in the given pile is less than or equal to the current number of stones in the pile
    if converted_list[0] > current_state[converted_list[1]-1]:
        return False, None
    
    return True, converted_list

def convert_input(input_string):
    input_string = input_string.split()
    input_list = []
    for each_item in input_string:
        input_list.append(each_item)
    return input_list

def is_integer(char):
    try:
        int(char)    
    except ValueError:
        return False
    return True

main()