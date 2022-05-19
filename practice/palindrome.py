def palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False


def main():
    print(palindrome("abb"))

if __name__ == "__main__":
    main()