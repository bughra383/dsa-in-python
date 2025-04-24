
def main():
    a = [1, 5 , 8 ,10]
    b = [5 , 11, 13, 19]
    c = []        
    n = len(a)

    for i in range(0, n):
        c.append(a[i] * b[i])

    print(c)

    
if __name__ == "__main__":
    main()