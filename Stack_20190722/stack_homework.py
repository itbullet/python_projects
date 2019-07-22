import stack_class

word_stack = stack_class.Stack()
word = "Yesterday"

for c in word:

    word_stack.push(c)

reverse = ""

print(len(word_stack.items))
print(word_stack.size())

for i in range(word_stack.size()):

    reverse += word_stack.pop()

print(reverse)