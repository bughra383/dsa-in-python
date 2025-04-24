
def main():
    lst = [x for x in range(10)]

    try:
        for i in range(0,11):
            print(lst[i])
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")

if __name__ == "__main__":
    main()