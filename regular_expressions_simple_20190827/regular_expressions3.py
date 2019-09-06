import re

str = "aRET#_62p@a aba ab#8Sba aZb4_Ab8ba abca abea #testTEST23"

matches = re.findall(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[_#])(?!.*[@/]).{10,}", str)

matches2 = re.findall(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[_#])(?!.*[@/])\S{10,}", str)

print(matches)

print(matches2)
