

def all_distinct(seq):
    return len(seq) == len(set(seq))

def main():
    lst = [int(input("Enter a value: ")) for _ in range(4)]

    if all_distinct(lst):
        print("All numbers are different from each other.")
    else:
        print("Not all numbers are different from each other.")

if __name__ == "__main__":
    main()
