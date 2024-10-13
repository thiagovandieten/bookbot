def main():
    with open('books/frankenstein.txt', 'r') as file:
        file_contents = file.read()
        print(file_contents)

main()