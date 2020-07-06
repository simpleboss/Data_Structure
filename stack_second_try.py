from node import Node


class Stack:
    def __init__(self, limit=None):
        self.size = 0
        self.limit = limit
        self.top_item = None

    def push(self, value):
        if self.has_space():
            item_to_push = Node(value)
            self.size += 1
            if self.top_item:
                item_to_push.set_next_node(self.top_item)
            self.top_item = item_to_push
        else:
            print("The Stack is full.")

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            return item_to_remove.get_value()
        else:
            print("The Stack is empty.")

    def peek(self):
        if not self.is_empty():
            item_to_peek = self.top_item
            return item_to_peek.get_value()
        else:
            print("The Stack is empty.")

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.limit > self.size


grocery = Stack(10)
grocery.push("Milk")
grocery.push("Chocolate")
print(grocery.pop())
print(grocery.pop())
print(grocery.pop())
