class TreeNode:
    def __init__(self, data, list_of_children=[]):
        self.data = data
        self.children = []
        self.add_child(list_of_children)

    def __str__(self, level=0):
        s = (" " * level) + str(self.data) + "\n"
        level += 1
        for child in self.children:
            s += (" " * level) + child.__str__(level)
        return s

    def get_node(self, data):
        for child in self.children:
            if child.data == data:
                return child


    def add_child(self, items, parent=None):
        if parent is None:
            for item in items:
                self.children.append(TreeNode(item))

        else:
            parent_node = self.get_node(parent)
            for item in items:
                parent_node.children.append(TreeNode(item))


drinks = TreeNode("DRINKS", ["HOT","COLD","WARM"])
print(drinks)
drinks.add_child(["TEA","COFFEE"], "HOT")
print(drinks)
drinks.add_child(["SODA","BEER"], "COLD")
print(drinks)
drinks.add_child(["CHOCOLATE"], "WARM")
print(drinks)
