import re


t = "__один__ __два__ __три__"


results = re.findall("__.*?__", t)


for match in results:
    print(match)
