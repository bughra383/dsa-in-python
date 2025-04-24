from random import randint

def shuffle(lst):
    length = len(lst)
    for i in range(length - 1 , 0 , -1):
        j = randint(0,i)
        lst[i], lst[j] = lst[j], lst[i]

    return lst


def main():
    lst = [x for x in range(10)]
    print(shuffle(lst))


if __name__ == "__main__":
    main()