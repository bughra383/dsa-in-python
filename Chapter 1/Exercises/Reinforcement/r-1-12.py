import random


def choice(lst):
    index = random.randrange(len(lst))
    return lst[index]

def main():
    lst = [i for i in range(1,100)]
    print(choice(lst))


if __name__ == "__main__":
    main()