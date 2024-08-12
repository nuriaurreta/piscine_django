def numbers():
    reader = open('numbers.txt', 'r')
    try:
        txt = reader.read().split(',')
        for n in txt:
            print(n)
    finally:
        reader.close()

if __name__ == '__main__':
    numbers()