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

def find_state():
    if len(sys.argv) != 2:
        return
    
    if sys.argv[1] in capital_cities.values():
        valor_cap = sys.argv[1]
        for k, v, in capital_cities.items():
            if v == valor_cap:
                capital = k
        if capital in states.values():
            valor_state = capital
        for key, value, in states.items():
            if value == valor_state:
                print(key)
    else:
        print('Unknown capital city')

if __name__ == '__main__':
    find_state()