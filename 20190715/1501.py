import re

l = "Красивое лучше, чем уродливое."

matches = re.findall("красивое", l, re.IGNORECASE)

print(matches)