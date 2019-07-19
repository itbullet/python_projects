l = list(range(12))
print(l)
print(l[1:3])
print(l[-1:])
print(l[::2])
l[0:1]=[-1,-1,-1]
print(l)
del l[:3]
print(l)