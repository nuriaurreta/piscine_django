#!/usr/bin/python3

from path import Path

def main():
    try:
        Path.makedirs('new_folder')
    except FileExistsError as e:
        print(e)
    f = Path('new_folder/hello')
    f.write_lines(['hello world!'])
    print(f.read_text())

if __name__ == '__main__':
    main()