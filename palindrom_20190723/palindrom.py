def palindrom(word):

    word = word.lower()

    return word[::-1] == word

print(palindrom("Mother"))
print(palindrom("Mum"))

s1 = "Test"

print(s1[::-1])