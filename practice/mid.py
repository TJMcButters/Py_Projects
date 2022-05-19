def mid(a):
    if len(a) % 2 == 0:
        return ""
    else:
        offset = int(len(a)/2)
        return a[offset]


def main():
    print(mid("abcdefg"))    

if __name__ == "__main__":
    main()