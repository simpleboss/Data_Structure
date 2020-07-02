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


father = Node("Dr Lee")
mother = Node("MK")
son1 = Node("Gichan")
son2 = Node("Gimoon")

father.set_next_node(mother)
mother.set_next_node(son1)
son1.set_next_node(son2)

# print(father.get_value())
# print(mother.get_next_node().get_value())
# print(son2.get_next_node())

