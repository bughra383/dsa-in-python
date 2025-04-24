from string import *

def delete_punctuation(str):
    chars_to_remove = set(punctuation)
    new_str = ''.join(char for char in str if char not in chars_to_remove)
    return new_str
    
def main():
    print(delete_punctuation(input("Enter a string: ")))


if __name__ == "__main__":
    main()