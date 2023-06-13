class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def pre_order_traversal(tree_node):
    if not tree_node:
        return
    else:
        print(tree_node.value)
        pre_order_traversal(tree_node.left_child)
        pre_order_traversal(tree_node.right_child)


def post_order_traversal(tree_node):
    if not tree_node:
        return
    else:
        post_order_traversal(tree_node.left_child)
        post_order_traversal(tree_node.right_child)
        print(tree_node.value)


def in_order_traversal(tree_node):
    if not tree_node:
        return
    else:
        in_order_traversal(tree_node.left_child)
        print(tree_node.value)
        in_order_traversal(tree_node.right_child)


class Queue:
    class Node:
        def __init__(self, value):
            self.data = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            node_to_return = self.head
            self.head = self.head.next

            return node_to_return

    def is_empty(self):
        if self.head:
            return False
        else:
            return True


def level_order_traversal(tree_node):
    if not tree_node:
        return
    else:
        q = Queue()
        q.enqueue(tree_node)

        while not q.is_empty():
            tree_node = q.dequeue().data
            print(tree_node.value)
            if tree_node.left_child is not None:
                q.enqueue(tree_node.left_child)
            if tree_node.right_child is not None:
                q.enqueue(tree_node.right_child)


def search(tree_node, value):
    if not tree_node:
        return
    else:
        q = Queue()
        q.enqueue(tree_node)

        while not q.is_empty():
            tree_node = q.dequeue().data
            if tree_node.value == value:
                return True
            if tree_node.left_child is not None:
                q.enqueue(tree_node.left_child)
            if tree_node.right_child is not None:
                q.enqueue(tree_node.right_child)

        return False


def insert_Binary_Tree(tree_node, new_node):
    if not tree_node:
        tree_node = new_node
        return
    else:
        q = Queue()
        q.enqueue(tree_node)

        while not q.is_empty():
            tree_node = q.dequeue().data

            if tree_node.left_child is None:
                tree_node.left_child = new_node
                return
            elif tree_node.right_child is None:
                tree_node.right_child = new_node
                return

            if tree_node.left_child is not None:
                q.enqueue(tree_node.left_child)
            if tree_node.right_child is not None:
                q.enqueue(tree_node.right_child)

def deepest_node(tree_node):
    if not tree_node:
        return None

    q = Queue()
    q.enqueue(tree_node)

    while not q.is_empty():
        node = q.dequeue().data
        if node.left_child is not None:
            q.enqueue(node.left_child)
        if node.right_child is not None:
            q.enqueue(node.right_child)

    return node

def delete_deepest_node(tree_node, deepest_node):
    if not tree_node:
        return
    else:
        q = Queue()
        q.enqueue(tree_node)

        while not q.is_empty():
            node = q.dequeue().data

            if node is deepest_node:
                node = None
                return
            elif node.left_child is deepest_node:
                node.left_child = None
                return
            elif node.right_child is deepest_node:
                node.right_child = None
                return

            if node.left_child is not None:
                q.enqueue(node.left_child)
            if node.right_child is not None:
                q.enqueue(node.right_child)

def delete_node_BT(tree_node, value_to_delete):
    if not tree_node:
        return

    q = Queue()
    q.enqueue(tree_node)
    while not q.is_empty():
        node = q.dequeue().data
        if node.value == value_to_delete:
            deepest = deepest_node(tree_node)
            deepest_value = deepest.value
            delete_deepest_node(tree_node, deepest)
            node.value = deepest_value
            return

        if node.left_child is not None:
            q.enqueue(node.left_child)

        if node.right_child is not None:
            q.enqueue(node.right_child)


def delete_node_Binary_Tree(tree_node, node_to_delete):
    pass

drinks = TreeNode("DRINKS")
hot = TreeNode("HOT")
cold = TreeNode("COLD")
drinks.left_child = hot
drinks.right_child = cold
hot.left_child = TreeNode("TEA")
hot.right_child = TreeNode("COFFEE")
cold.left_child = TreeNode("BEER")
cold.right_child = TreeNode("SODA")

pre_order_traversal(drinks)
print(".....")
post_order_traversal(drinks)
print(".....")
in_order_traversal(drinks)
print(".....")
level_order_traversal(drinks)

print(".....")
print(search(drinks, "SODA"))
print(search(drinks, "EBO"))
print(".....")
insert_Binary_Tree(drinks, TreeNode("EBO"))
pre_order_traversal(drinks)
print(".....")
insert_Binary_Tree(drinks, TreeNode("ESTEE"))
pre_order_traversal(drinks)
print(".....")
insert_Binary_Tree(drinks, TreeNode("JOJO"))
pre_order_traversal(drinks)
print(".....")
delete_node_BT(drinks, "HOT")
pre_order_traversal(drinks)
