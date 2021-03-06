from node import Node


class Stack:
    def __init__(self, name, limit):
        self.top_item = None
        self.name = name
        self.size = 0
        self.limit = limit

    def push(self, value):
        if not self.is_full():
            new_node = Node(value)
            new_node.set_next_node(self.top_item)
            self.top_item = new_node
            self.size += 1
        else:
            print("Stacks is full")

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return_item = self.top_item
            self.top_item = return_item.get_next_node()
            return return_item.get_value()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Stack is empty")

    def list_of_nodes(self):
        current_node = self.top_item
        result = []
        while current_node:
            result.append(current_node.get_value())
            current_node = current_node.get_next_node()
        result.reverse()
        return result

    def is_full(self):
        return self.limit <= self.size

    def is_empty(self):
        return self.size == 0


# stack = Stack(10)
# stack.push("first card")
# stack.push("second card")
# stack.push("third card")
# print(stack.pop())
# print(stack.peek())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.list_of_nodes())
