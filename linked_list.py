from node import MemberNode


class GroupLinkedList:
    def __init__(self, node):
        self.head_node = node

    def get_head_node(self):
        return self.head_node

    def set_head_node(self, node):
        self.head_node = node

    def insert_beginning(self, value):
        new_node = MemberNode(value)
        new_node.set_next_node(self.get_head_node)
        self.set_head_node(new_node)

    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        while current_node:
            string_list += str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return string_list


son2 = MemberNode("Gimoon")
son1 = MemberNode("Gichan", son2)
mother = MemberNode("MK", son1)
father = MemberNode("Dr Lee", mother)

family = GroupLinkedList(father)
print(family.stringify_list())

