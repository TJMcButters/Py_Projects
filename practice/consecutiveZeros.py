def consecutive_zeros(a):
    zeros = ""
    count = []
    for x in a:
        if x == '0':
            zeros += '0'
        else:
            count.append(zeros)
            zeros = ""
            
    longest = -1
    for x in count:
        if len(x) > longest:
            longest = len(x)
    return longest            
            


def main():
    print(consecutive_zeros("10000010000000000000"))
    
if __name__ == "__main__":
    main()