#!/usr/bin/python3

d=[
('Hendrix' , '1942'), ('Allman' , '1946'),
('King' , '1925'), ('Clapton' , '1945'),
('Johnson' , '1911'), ('Berry' , '1926'),
('Vaughan' , '1954'), ('Cooder' , '1947'),
('Page' , '1944'), ('Richards' , '1943'),
('Hammett' , '1962'), ('Cobain' , '1967'),
('Garcia' , '1942'), ('Beck' , '1944'),
('Santana' , '1947'), ('Ramone' , '1948'),
('White' , '1975'), ('Frusciante', '1970'),
('Thompson' , '1949'), ('Burton' , '1939')
]

def main():
    my_dict = dict(d)
    final_d = {}
    for k, v in my_dict.items():
        final_d[v] = k
    for k, v in final_d.items():
        print(f"{k} : {v}")
   
if __name__ == '__main__':
    main()