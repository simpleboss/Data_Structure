from node_second_try import Node


class LinkedList:
    def __init__(self, name):
        self.name = name
        self.head_node = None

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def remove_first_node_which_has_this_value(self, value):
        current_node = self.head_node
        while current_node:
            next_node = current_node.get_next_node()
            if next_node.get_value() == value:
                current_node.set_next_node(next_node.get_next_node())
                break
            current_node = next_node

    def stringify_list(self):
        result_list = []
        current_node = self.head_node
        while current_node:
            result_list.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return result_list


# family = LinkedList("family")
# family.insert_beginning("Gimoon")
# family.insert_beginning("Gichan")
# family.insert_beginning("MK")
# family.insert_beginning("Andy")
# family.remove_first_node_which_has_this_value("Gichan")
#
# print(family.stringify_list())
