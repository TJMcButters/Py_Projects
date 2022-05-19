def add_dots(a):
    new_word = []
    new_string = ""
    for x in range(len(a)):
        new_word.append(a[x])
        new_word.append(".")
    new_word = new_word[:-1]
    for let in new_word:
        new_string += let
    return new_string
    
def remove_dots(a):
    new_word = ""
    for let in a:
        if let != ".":
            new_word += let
    return new_word

def main():
    h = "hello"
    dots = add_dots(h)
    print(dots)
    no_dots = remove_dots(dots)
    print(no_dots)


if __name__ == "__main__":
    main()