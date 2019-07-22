import os
filepath = os.path.join("c:",
            "\\",
            "test",
            "test1",
            "test2.txt")

print(filepath)

with open(filepath, "r") as f:
    print(f.read())
