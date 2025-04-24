from string import *

def delete_punctuation(str):
    translation_table = str.maketrans("", "", punctuation)
    return str.translate(translation_table)
    
def main():
    print(delete_punctuation(input("Enter a string: ")))


if __name__ == "__main__":
    main()