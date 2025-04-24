def count_vowels(string):
    vowels = set("aeiouAEIOU")
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
            
    return count


def main():
    print(count_vowels(input()))

if __name__ == "__main__":
    main()