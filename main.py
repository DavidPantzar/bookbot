def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_letters(text)
    sorted_characters = sort_dictionary(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n\n")

    for character in sorted_characters:
        print(f"The '{character[0]}' character was found {character[1]} times")
    


def get_num_words(string):
    return len(string.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_letters(string):
    character_dict = {}
    lower_string = string.lower()
    for character in lower_string:
        character_dict.setdefault(character, 0)

    for character in lower_string:
        value = character_dict.get(character)
        value += 1
        character_dict.update({character: value})

    return character_dict

def sort_dictionary(dictionary):
    list_of_characters = list(dictionary.items())
    new_list = []

    for character in list_of_characters:
        if character[0].isalpha():
            new_list.append(character)
    
    new_list.sort()
    return new_list

main()

