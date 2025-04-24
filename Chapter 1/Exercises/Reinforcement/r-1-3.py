

def minmax(array):
    array.sort()
    minmax = (array[0], array[-1])
    return minmax 


def main():
    arr = [1, 15, 123, 9, 131, 2, 1000]    
    print(minmax(arr))

if __name__ == "__main__":
    main()



    
