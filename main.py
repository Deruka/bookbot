def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        amount_words = count_words(file_contents)
        amount_characters = count_characters(file_contents)
        print(f"the book contains {amount_words} words")
        print(amount_characters)

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

main()
