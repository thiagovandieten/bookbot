def count_words_in_file(content_list):
    return len(content_list)

def count_characters_in_file(content_list):
    character_count = {}

    for word in content_list:
        characters = list(word)
        for c in characters:
            if not c.isalpha():
                continue
           
            c = c.casefold() # lowercase so we don't count captialized letters
            if c not in character_count:
                character_count[c] = 0
            character_count[c] += 1
   
    sorted_list = sorted(character_count.items(), key=lambda x:x[1], reverse=True) # Lambda functions explained: https://www.w3schools.com/python/python_lambda.asp
    return dict(sorted_list)

def print_character_count(character_count):
    for char, count in character_count.items():
        print(f"The character '{char}' was found {count} times")

def main():
    with open('books/frankenstein.txt', 'r') as file:
        file_contents = file.read()
        print(f"--- Begin report of books/frankenstein.txt ---")
        contents_in_list = file_contents.split()
        
        count_words = count_words_in_file(contents_in_list)
        print(f"{count_words} words in the document\n")

        character_count = count_characters_in_file(file_contents)
        print_character_count(character_count)

main()