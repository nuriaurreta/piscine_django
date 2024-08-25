#!/usr/bin/python3

def main():
    vars = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]

    for var in vars:
        print(f"{var} has a type {type(var)}")

if __name__ == '__main__':
    main()
