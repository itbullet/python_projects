str = input("What is your name?")

with open("homework2.txt","w") as f:
    f.write(str)