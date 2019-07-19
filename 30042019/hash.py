h1 = {1:"one", 2:"two", 3:"three"}
h2 = {0:"zero", 5:"five"}
h3 = {1:"z", 2:"y", 3:"x"}

for key, value in h1.items():
	print(key, " ", value)
	
for key in h2.keys():
	print(key, " ", h2[key])

for v in h3.values():
	print(v)
	
print(h1)

h1.update(h3)

print(h1)	

print(len(h3))