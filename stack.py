from node import Node


class Stack:
    def __init__(self, limit):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if not self.is_full():
            new_node = Node(value)
            self.top_item = new_node
            self.size += 1
        else:
            print("Stacks is full")

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.top_item
        else:
            print("Stack is empty")

    def peek(self):
        pass

    def is_full(self):
        return self.limit <= self.size

    def is_empty(self):
        return self.size == 0


stack = Stack(10)
stack.push("one card")
stack.pop()

