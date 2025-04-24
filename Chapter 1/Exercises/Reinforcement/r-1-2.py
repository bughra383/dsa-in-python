
def main():
    print(is_even(1))
    print(is_even(2))


def is_even(k):
    if k & 1 == 0: # bitwise operator checks lsb
        return True
    else:
        return False


if __name__ == "__main__":
    main()