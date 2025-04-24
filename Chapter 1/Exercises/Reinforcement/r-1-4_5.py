

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n))

def main():
    try:
        n = int(input("Enter a positive number: "))
        if n > 0:
            print(sum_of_squares(n))
        else:
            print("Enter a positive number")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
