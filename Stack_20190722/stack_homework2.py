import stack_class

number_stack = stack_class.Stack()

number_list = [1, 2, 3, 4, 5]

print(number_list)

"""Version 1
for i in range(len(number_list)):
    num = number_list[i]
    #print(str(i) + " " + str(num))
    number_stack.push(num)
"""
#Version 2
for item in number_list:
    #print(item)
    number_stack.push(item)

number_list.clear()

"""
print("**********")
print(number_list)
print(number_stack.peek())
print("**********")
"""

for i in range(number_stack.size()):

    num = number_stack.pop()

    #print(num)

    number_list.append(num)

print(number_list)