import re

str = "Привидение прошуршало и и исчезло в углу ло"

found = re.findall("\w*ло\w*", str, re.IGNORECASE)

for match in found:
    print(match)


emails = "gur-u99.ed.start36.com@goog-le.com, careerguru99@hotmail.com, users@yahoomail.com test @mest test@"
email = re.findall("[\w\.-]+@[\w\.-]+", emails)
#print(email)

for item in email:
    print(item)