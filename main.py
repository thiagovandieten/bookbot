def count_words_in_file(content):
    contents_in_list = content.split()
    return len(contents_in_list)

def main():
    with open('books/frankenstein.txt', 'r') as file:
        file_contents = file.read()
        print(file_contents)

        print(count_words_in_file(file_contents))

main()