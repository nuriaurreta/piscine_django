import sys

states = {
    "Oregon": "OR", 
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

# function that filters the arguments
def get_args(input_str):
    input_list = input_str.split(',')
    filtered_list = [s.strip() for s in input_list if s.strip()]
    arg_list = [s.lower() for s in filtered_list]
    return arg_list

# function that find if the arguments are in the data and if are correct
def find_all():
    if len(sys.argv) != 2:
        return
    
    input_str = sys.argv[1]
    to_find = get_args(input_str)

    for arg in to_find:
        found = False
        
        # looks if the argument is a state
        for state, abr in states.items():
            if arg == state.lower():
                print(f'{capital_cities[abr]} is the capital of {state}')
                found = True
                break
        
        # looks if the argument is a capital
        if not found:
            for abr, cap in capital_cities.items():
                if arg == cap.lower():
                    for state_name, state_abr in states.items():
                        if abr == state_abr:
                            print(f'{cap} is the capital of {state_name}')
                            found = True
                            break
        
        if not found:
            print(f'{arg} is neither a capital city nor a state')

if __name__ == '__main__':
    find_all()
