import re


line = "Я люблю $"


m = re.findall("\\$",
               line,
               re.IGNORECASE)

print(m)
