# Write a Python program to create a class representing a stack data structure.
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    stack.push(4)
    print(stack)
    print(stack.pop())
    print(stack)