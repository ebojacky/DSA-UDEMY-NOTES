class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_BSTnode(root_node, value):
    if root_node.value is None:
        root_node.value = value
    elif value <= root_node.value:
        if root_node.left is None:
            root_node.left = BSTNode(value)
        else:
            insert_BSTnode(root_node.left, value)
    else:
        if root_node.right is None:
            root_node.right = BSTNode(value)
        else:
            insert_BSTnode(root_node.right, value)


def in_order_traversal_BST(root_node):
    if root_node is None:
        return
    in_order_traversal_BST(root_node.left)
    print(root_node.value)
    in_order_traversal_BST(root_node.right)


def pre_order_traversal_BST(root_node):
    if root_node is None:
        return
    print(root_node.value)
    in_order_traversal_BST(root_node.left)
    in_order_traversal_BST(root_node.right)


def level_order_traversal_BST(root_node):
    if root_node is None:
        return

    node_list = []
    node_list.append(root_node)

    while len(node_list) > 0:
        node = node_list.pop(0)
        print(node.value)
        if node.left is not None:
            node_list.append(node.left)
        if node.right is not None:
            node_list.append(node.right)


def search_BST(root_node, value):
    if value == root_node.value:
        print("FOUND")
    if value < root_node.value:
        if root_node.left:
            search_BST(root_node.left, value)
    else:
        if root_node.right:
            search_BST(root_node.right, value)


def minimum(root_node):
    min = root_node

    while root_node.left:
        min = root_node.left
        root_node = root_node.left

    return min


def delete_node_in_BST(root_node, value):
    if not root_node:
        return root_node
    if value < root_node.value:
        root_node.left = delete_node_in_BST(root_node.left, value)
    elif value > root_node.value:
        root_node.right = delete_node_in_BST(root_node.right, value)
    else:
        # Childless node (leaf node). Set to None
        if root_node.left is None and root_node.right is None:
            root_node = None
        # Only right child. Set to right child
        elif root_node.left is None:
            root_node = root_node.right
        # Only left child. Set to left child
        elif root_node.right is None:
            root_node = root_node.left
        # Has 2 children. Set node to min on the right branch. delete min on the right branch
        else:
            min_node = minimum(root_node.right)
            root_node.value = min_node.value
            root_node.right = delete_node_in_BST(root_node.right, min_node.value)

    return root_node


def delete_BST(root_node):
    root_node.value = None
    root_node.left = None
    root_node.right = None


my_bst = BSTNode(10)
for value in [500, 1500, 7, 2, 3, 1001, 6000, 7000,55]:
    insert_BSTnode(my_bst, value)
in_order_traversal_BST(my_bst)
print("___")
level_order_traversal_BST(my_bst)
print("___")
search_BST(my_bst, 13)
print(minimum(my_bst).value)
print("___")
level_order_traversal_BST(my_bst)
print("Deleting___")
delete_node_in_BST(my_bst, 10)
level_order_traversal_BST(my_bst)
