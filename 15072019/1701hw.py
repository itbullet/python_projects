import re

with open("zen.txt", "r") as f:
    text = f.read()
    print(text)

match = re.findall("голландец", text, re.IGNORECASE)

print(match)
