class Stack:

    def __init__(self):

        self.items = []

    def is_empty(self):

        return self.items == []

    def push(self, item):

        self.items.append(item)

    def pop(self):

        return self.items.pop()

    def peek(self):

        last = len(self.items) - 1

        return self.items[last]

    def size(self):

        return len(self.items)


stack = Stack()

"""print(stack.is_empty())

stack.push(21)

print(stack.is_empty())

item = stack.pop()

print(item)

print(stack.is_empty())

for i in range(0, 6):

    stack.push(i)

print(stack.peek())

print(stack.size())

print(stack.pop())

print(stack.size())"""

for c in "Hello":

    stack.push(c)

reverse = ""

for i in range(len(stack.items)):

    reverse += stack.pop()

print(reverse)