
a, b, c = [int(input(f"Enter value {i+1}: ")) for i in range(3)]

if a + b == c:
    print(f"{a} + {b} = {c}")
elif a == b - c:
    print(f"{a} = {b} - {c}")
elif a * b == c:
    print(f"{a} * {b} = {c}")
else:
    print("The values cannot form a correct arithmetic formula in the given order.")