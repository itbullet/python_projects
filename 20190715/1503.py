import re

string = " Двас даа."

m = re.findall("д[ав]а", string, re.IGNORECASE)

print(m)