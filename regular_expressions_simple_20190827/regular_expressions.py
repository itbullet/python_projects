import re

str = "ahb acb aeb aeeb adcb axeb"

matches = re.findall("a.b", str)

print(matches)
