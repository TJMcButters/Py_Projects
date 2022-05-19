from curses.ascii import isupper


def capital_indexes(a):
    index = []
    for pos in range(len(a)):
        if isupper(a[pos]):
            index.append(pos)
    return index
            

def main():
    x = capital_indexes("HeLlO")
    for i in x:
        print(i)
        
if __name__ == "__main__":
    main()