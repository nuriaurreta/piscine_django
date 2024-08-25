#!/usr/bin/python3

d={
    'Hendrix' : '1942', 'Allman' : '1946',
    'King' : '1925', 'Clapton' : '1945',
    'Johnson' : '1911', 'Berry' : '1926',
    'Vaughan' : '1954', 'Cooder' : '1947',
    'Page' : '1944', 'Richards' : '1943',
    'Hammett' : '1962', 'Cobain' : '1967',
    'Garcia' : '1942', 'Beck' : '1944',
    'Santana' : '1947', 'Ramone' : '1948',
    'White' : '1975', 'Frusciante': '1970',
    'Thompson' : '1949', 'Burton' : '1939',
}

def main(dic):
    """ (dic.items() -> creates a list of tuples from the dictionary
    sorted(..., key=lambda item: (item[1], item[0]) -> order the list
    first from the value (item[1] in the tuple) and then from the key
    (item[0] in the tuple)
    """
    sorted_dict = sorted(dic.items(), key=lambda item: (item[1], item[0]))
    for tup in sorted_dict:
        print(tup[0])

if __name__ == '__main__':
    main(d)