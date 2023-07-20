# word_counter.py

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    input_file = "portfolio.txt"  # Replace this with the name of your input file.
    text = read_file(input_file)
    print("Text content:")
    print(text)

    word_count = count_words(text)
    print("\nWord count:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
