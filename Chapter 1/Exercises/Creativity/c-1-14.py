import itertools

lst = [int(input("Enter a value: ")) for i in range(1,5)]

odd_pair = any((x * y) % 2 == 1 for x, y in itertools.combinations(lst, 2))

if odd_pair:
    print("There is a pair with an odd product.")
else:
    print("No pair with an odd product.")