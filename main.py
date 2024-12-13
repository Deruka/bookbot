def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        amount_words = count_words(file_contents)
        amount_characters = count_characters(file_contents)
        list_of_dicts = [{'character': key, 'num': value} for key, value in amount_characters.items()]
        list_of_dicts.sort(reverse=True, key=sort_on)
        # Report Print
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{amount_words} words found in the document")
        print(" ")
        for item in list_of_dicts:
            print(f"The '{item['character']}' character was found {item['num']} times")
        print("--- End report ---")

def count_words(file_to_count):
    words = file_to_count.split()
    count = len(words)
    return count

def count_characters(file_to_count):
    characters = {}
    words_lower = file_to_count.lower()
    for character in words_lower:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters

def sort_on(dict):
    return dict["num"]

main()
