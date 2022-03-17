class Stack:
    def __init__(self):
        self.data = []
        self.maximum = []

    def push(self, data):
        if not self.data or data >= self.max():
            self.maximum.append(data)
        self.data.append(data)

    def pop(self):
        if not self.data:
            raise Exception('Stack is empty.')
        if self.data[-1] == self.max():
            self.maximum.pop()
        return self.data.pop()

    def max(self):
        if not self.data:
            raise Exception('Stack is empty.')
        return self.data[-1] if not self.maximum else self.maximum[-1]

#Test run
stack = Stack()

stack.push(3)
stack.push(5)
print(stack.max())
stack.push(7)
stack.push(19)
print(stack.max())
stack.pop()
print(stack.max())
