from pyparsing import empty


class Stack:
    length = 99
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, data):
        if not isinstance(data, int):
            raise TypeError('Data должна быть целочисленного типа')
        if len(self.stack) < Stack.length:
            self.stack.append(data)
        else:
            print('Stack is full')

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return('Stack is empty')

    def empty(self):
        return len(self.stack) == 0

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.empty())
stack.pop()
print(stack.empty())
print(stack.pop())