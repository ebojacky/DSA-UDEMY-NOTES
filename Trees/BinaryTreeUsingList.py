class BinaryTreeWithList:
    def __init__(self, size):
        self.size = size
        self.nodes = size * [None]
        self.last_used_index = 0

    def print(self):
        for node in self.nodes:
            print(node)


    def insert(self, value):
        if self.last_used_index + 1 >= self.size:
            return
        self.nodes[self.last_used_index + 1] = value
        self.last_used_index += 1

    def search(self, value):
        for node in self.nodes:
            if node == value:
                return True
        return False

    def pre_order_traversal(self, index):
        if index > self.last_used_index or index == 0:
            return
        print(self.nodes[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal((index * 2) + 1)

    def post_order_traversal(self, index):
        if index > self.last_used_index or index == 0:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal((index * 2) + 1)
        print(self.nodes[index])

    def in_order_traversal(self, index):
        if index > self.last_used_index or index == 0:
            return
        self.in_order_traversal(index * 2)
        print(self.nodes[index])
        self.in_order_traversal((index * 2) + 1)

    def level_order_traversal(self, index):
        if index == 0 or index > self.last_used_index:
            return
        for i, node in enumerate(self.nodes):
            if i >= index:
                print(node)

    def delete_node(self, value):
        for index, node in enumerate(self.nodes):
            if node == value:
                self.nodes[index] = self.nodes[self.last_used_index]
                self.nodes[self.last_used_index] = None
                self.last_used_index -= 1

    def delete_BT(self):
        self.nodes = self.size * [None]
        self.last_used_index = 0


my_bin_tree = BinaryTreeWithList(8)
my_bin_tree.print()
my_bin_tree.level_order_traversal(1)
my_bin_tree.insert("N1")
my_bin_tree.insert("N2")
my_bin_tree.insert("N3")
my_bin_tree.insert("N4")
my_bin_tree.insert("N5")
my_bin_tree.insert("N6")
my_bin_tree.insert("N7")
my_bin_tree.insert("N8")
my_bin_tree.insert("N9")
my_bin_tree.insert("N10")

my_bin_tree.level_order_traversal(1)
print(my_bin_tree.search("N10"))
print(my_bin_tree.search("N2"))

my_bin_tree.pre_order_traversal(1)
print("----")
my_bin_tree.post_order_traversal(1)
print("----")
my_bin_tree.in_order_traversal(1)
print("----")
my_bin_tree.level_order_traversal(1)
print("----")
my_bin_tree.delete_node("N5")
my_bin_tree.level_order_traversal(1)
print("----")
my_bin_tree.delete_BT()
my_bin_tree.level_order_traversal(1)
my_bin_tree.print()