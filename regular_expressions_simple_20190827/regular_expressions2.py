import re

str = "aa aba abba abbba abca abea"

matches = re.findall(r"\b[a-b]+\b", str)

print(matches)
