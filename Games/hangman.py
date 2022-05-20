from random import randint

def word_picker():
    words = ["hello", "goodbye", "dog", "cat"]
    return words[randint(0, len(words))]


def main():
    print(word_picker())

if __name__ == "__main__":
    main()
