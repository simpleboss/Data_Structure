from node import Node


class Stacks:
    def __init__(self, limit):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_full(self):
        return self.limit <= self.size

    def is_empty(self):
        return self.size == 0
