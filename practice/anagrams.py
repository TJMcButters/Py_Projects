def is_anagram(a, b):
    
    x = sorted(a.lower())
    y = sorted(b.lower())
    
    if x == y:
        return True
    else:
        return False


def main():
    print(is_anagram("eloh", "eLLoh"))

if __name__ == "__main__":
    main()