class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

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


def level_order_traversal(root_node: AVLTreeNode):
    if not root_node:
        return

    q = Queue()
    q.enqueue(root_node)

    while q.is_empty() is False:
        node = q.dequeue().data
        print(node.data)
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)

def search_avl(root_node: AVLTreeNode, value):
    # using pre-order traversal
    if not root_node:
        return False

    if value == root_node.data:
        return True
    else:
        found = search_avl(root_node.left, value)
        if found:
            return True
        found = search_avl(root_node.right, value)
        return found

def get_height(root_node: AVLTreeNode):
    if not root_node:
        return 0
    return root_node.height

def get_balance_indicator(root_node):
    if not root_node:
        return 0
    balance_indicator = get_height(root_node.left) - get_height(root_node.right)
    return balance_indicator

def rotate_right(root_node: AVLTreeNode):
    if not root_node:
        return
    new_node = root_node.left
    print(f"trying to rotate {root_node.data}")
    root_node.left = root_node.left.right
    new_node.right = root_node

    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))
    new_node.height = 1 + max(get_height(new_node.left), get_height(new_node.right))

    return new_node

def rotate_left(root_node: AVLTreeNode):
    if not root_node:
        return
    new_node = root_node.right
    root_node.right = root_node.right.left
    new_node.left = root_node

    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))
    new_node.height = 1 + max(get_height(new_node.left), get_height(new_node.right))

    return new_node


def insert_avl(root_node: AVLTreeNode, value: int):
    if not root_node:
        return AVLTreeNode(value)
    elif not root_node.data:
        root_node.data = value
        return root_node
    elif value <= root_node.data:
        root_node.left = insert_avl(root_node.left, value)
    elif value > root_node.data:
        root_node.right = insert_avl(root_node.right, value)

    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))

    bi = get_balance_indicator(root_node)

    if bi > 1 and value < root_node.left.data:
        return rotate_right(root_node)
    if bi > 1 and value > root_node.left.data:
        root_node.left = rotate_left(root_node.left)
        return rotate_right(root_node)
    if bi < -1 and value > root_node.right.data:
        return rotate_left(root_node)
    if bi < -1 and value < root_node.right.data:
        root_node.right = rotate_right(root_node.right)
        return rotate_left(root_node)

    return root_node

def minimum(root_node: AVLTreeNode):
    if not root_node:
        return root_node

    min = root_node
    while min.left:
        min = min.left
    return min

def delete_avl(root_node: AVLTreeNode, value: int):
    if not root_node:
        return None
    elif value < root_node.data:
        root_node.left = delete_avl(root_node.left, value)
    elif value > root_node.data:
        root_node.right = delete_avl(root_node.right, value)
    else:
        if root_node.left is None:
            temp = root_node.right
            root_node = None
            return temp
        elif root_node.right is None:
            temp = root_node.left
            root_node = None
            return temp
        else:
            min_node = minimum(root_node.right)
            root_node.data = min_node.data
            root_node.right = delete_avl(root_node.right, min_node.data)

    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))

    bi = get_balance_indicator(root_node)

    if bi > 1 and get_balance_indicator(root_node.left) >= 0:
        return rotate_right(root_node)
    if bi > 1 and get_balance_indicator(root_node.left) < 0:
        root_node.left = rotate_left(root_node.left)
        return rotate_right(root_node)
    if bi < -1 and get_balance_indicator(root_node.right) <= 0:
        return rotate_left(root_node)
    if bi < -1 and get_balance_indicator(root_node.right) > 0:
        root_node.right = rotate_right(root_node.right)
        return rotate_left(root_node)


    return root_node


my_avl = AVLTreeNode(1000)
my_avl = insert_avl(my_avl, 50)
my_avl = insert_avl(my_avl, 5000)
my_avl = insert_avl(my_avl, 5)
my_avl = insert_avl(my_avl, 55)
my_avl = insert_avl(my_avl, 6000)
my_avl = insert_avl(my_avl, 8000)
print("____")
level_order_traversal(my_avl)
print(search_avl(my_avl, 8000))
my_avl = insert_avl(my_avl, 1)
my_avl = insert_avl(my_avl, 2)
my_avl = insert_avl(my_avl, 3)
print("____")
level_order_traversal(my_avl)
my_avl = insert_avl(my_avl, 40000)

print("____")
level_order_traversal(my_avl)
my_avl = delete_avl(my_avl, 1000)
print("__deleting__")
level_order_traversal(my_avl)

