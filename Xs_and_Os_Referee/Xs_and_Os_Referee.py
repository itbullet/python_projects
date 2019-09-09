list1 = ["OO.",
        "XOX",
        "XOX"]

if len(list1) == 3:
    print("True")
print(all(len(row) == 3 for row in list1))

