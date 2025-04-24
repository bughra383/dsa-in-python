"""
Pseudo-code

Initialize:
    list = [1, 2, 3, 4, 5]
    i = 0
    j = length(list) - 1

    while i < j:
        # Swap the elements
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

        # Update i and j
        i = i + 1
        j = j - 1

    # Print the list
    print(list)

"""


lst = [1, 2, 3, 4, 5]

i = 0
j = len(lst) - 1

while i < j:
    lst[i], lst[j] = lst[j], lst[i]
    i += 1
    j -= 1

print(lst)  # [5, 4, 3, 2, 1]
