def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        amount_words = count_words(file_contents)
        print(f"the book contains {amount_words} words")

def count_words(file_to_count):
    words = file_to_count.split()
    count = len(words)
    return count

main()
