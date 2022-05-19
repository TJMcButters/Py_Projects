def all_equal(a):
    num = a[0]
    for x in a:
        if x != num:
            return False
    return True


def main():
    x = [1, 1, 2]
    print(all_equal(x))

if __name__ == "__main__":
    main()