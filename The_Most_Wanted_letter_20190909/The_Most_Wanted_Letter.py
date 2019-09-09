def checkio(text: str) -> str:

    chr_max = ''
    quantity_max = 0
    text_temp = sorted(text.lower())

    for char in text_temp:

        if text_temp.count(char)> quantity_max and char != chr_max and char.isalpha():
            chr_max = char
            quantity_max = text_temp.count(char)

    #replace this for solution
    return chr_max

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")