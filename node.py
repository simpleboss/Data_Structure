class Member_node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node


father = Member_node("Dr Lee")
mother = Member_node("MK")
son1 = Member_node("Gichan")
son2 = Member_node("Gimoon")

father.set_link_node(mother)
mother.set_link_node(son1)
son1.set_link_node(son2)

print(father.get_value())
print(mother.get_link_node())
print(son2.get_link_node())

