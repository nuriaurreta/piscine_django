import settings
import sys
import os

def main():
    if len(sys.argv) != 2:
        return print("Error: incorrect number of arguments")
    input_file = sys.argv[1]
    _, extension = os.path.splitext(input_file)
    if extension != '.template':
        return print("Error: incorrect file extension")
    if not os.path.exists(input_file):
        return print(f"Error: file '{input_file}' does not exist")

    try:
        with open(input_file, 'r') as f:
            file_content = f.read()
            content = file_content.format(
                name=settings.name,
                surname=settings.surname,
                age=settings.age,
                profession=settings.profession,
            )
    except Exception as e:
        return print(f"Error processing file: {e}")

    output_file = f"{os.path.splitext(input_file)[0]}.html"
    try:
        with open(output_file, 'w') as f:
            f.write(content)
        print(f"File '{output_file}' has been successfully created.")
    except Exception as e:
        return print(f"Error writing output file: {e}")

if __name__ == '__main__':
    main()