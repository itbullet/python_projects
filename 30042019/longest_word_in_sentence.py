str = input()
length = 0
longest = ''
for word in str.split(" "):
	if len(word) > length: 
		longest = word

print(longest)