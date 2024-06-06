
def count_characters(sentence:str):
    return {char: sentence.count(char) for char in set(sentence) if char.isalpha()}

def main():
    with open("./book/frankenstein.txt") as f:
        file_content = f.read().lower()
        [print(f"The '{char}' character was found {count} times") for char, count in count_characters(file_content).items()]


if __name__ == "__main__":
    main()
