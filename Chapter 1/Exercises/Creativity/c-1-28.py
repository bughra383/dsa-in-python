
def norm(v, p=2):
    if p == float('inf'):
        return max(abs(x) for x in v)
    return sum(abs(x)**p for x in v)**(1/p)


def main():
    print(norm([4]))


if __name__ == "__main__":
    main()