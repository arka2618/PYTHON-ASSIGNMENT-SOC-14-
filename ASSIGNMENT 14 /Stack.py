class Stack():
    def __init__(self):
        self.stack = [10, 19, 24, 35, 46, 70]
    def push(self, item):
        self.stack.append(item)
        print(f"New Stack 1: {self.stack}")
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            self.stack.pop()
            print(f"{self.stack}")
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack is not Empty")
            print(self.stack[-1])
    def is_empty(self):
        if len(self.stack) == 0:
            print("Stack is empty")

s = Stack()
n = int(input("Enter a value you want to operate on: "))
s.push(n)
s.pop()
s.peek()
s.is_empty()

