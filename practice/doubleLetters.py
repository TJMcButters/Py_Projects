def double_letters(a):
    length = len(a)
    for x in range(length):
        if x == length - 1:
            return False
        if a[x] == a[x + 1]:
            return True
    return False
        
def main():
    print(double_letters("Hello"))

if __name__ == "__main__":
    main()