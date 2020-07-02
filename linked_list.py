from node import Node


class GroupLinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def set_head_node(self, node):
        self.head_node = node

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.get_head_node())
        self.set_head_node(new_node)

    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        while current_node:
            string_list += str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value):
        current_node = self.get_head_node()
        while current_node:
            next_node = current_node.get_next_node()
            if next_node.get_value() == value:
                current_node.set_next_node(next_node.get_next_node())
                return
            current_node = current_node.get_next_node()


family = GroupLinkedList("Gimoon")
family.insert_beginning("Gichan")
family.insert_beginning("MK")
family.insert_beginning("Father")

print(family.stringify_list())

family.remove_node("MK")

print("========")
print(family.stringify_list())
