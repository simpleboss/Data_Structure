class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# node1 = Node("Gichan")
# node2 = Node("Gimoon", node1)
# print(node2.get_next_node().get_value())