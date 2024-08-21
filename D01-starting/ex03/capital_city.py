import sys

states = {
    "Oregon" : "OR", 
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def find_capital():
    if len(sys.argv) != 2:
        return
    
    if sys.argv[1] in states:
        state = states[sys.argv[1]]
        if state in capital_cities:
            print(capital_cities[state])
    else:
        print('Unknown state')

if __name__ == '__main__':
    find_capital()