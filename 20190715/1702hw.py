import re

str = "Moscow: 777, 999, 797. New-York: 071, 950, 112."

match = re.findall("\d", str)

print(match)