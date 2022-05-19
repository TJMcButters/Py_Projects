from random import randint

def random_number():
    return randint(0, 101)


def main():
    counter = 0
    above = 0
    below = 0
    while counter < 100:
        r = random_number()
        if r > 50:
            above += 1
        else:
            below += 1
        print("{}: {}".format(counter + 1, r))
        counter += 1
    print(f"Above: {above}\nBelow: {below}")
    

if __name__ == "__main__":
    main()