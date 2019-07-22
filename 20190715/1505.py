import re

t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

#print(found)

for match in found:
    print(match)