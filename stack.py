from node import Node


class Stacks:
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
        pass

    def peek(self):
        pass

    def is_full(self):
        return self.limit <= self.size

    def is_empty(self):
        return self.size == 0


stacks = Stacks(10)
stacks.push("one card")
