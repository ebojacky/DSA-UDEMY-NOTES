################# 1 #################
"""
Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

Examples

customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }

g = Graph(customDict)
g.checkRoute("a", "j") #True
"""
from pprint import pprint


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
        # TODO
        # lets use Breath search first approach

        queue = []
        visited = []
        queue.append(startNode)

        while queue:
            current_node = queue.pop(0)
            visited.append(startNode)
            if endNode in self.gdict[current_node]:
                return True
            else:
                for edge in self.gdict[current_node]:
                    if edge not in visited:
                        queue.append(edge)

        return False


customDict = {"a": ["c", "d", "b"],
              "b": ["j"],
              "c": ["g"],
              "d": [],
              "e": ["f", "a"],
              "f": ["i"],
              "g": ["d", "h"],
              "h": [],
              "i": [],
              "j": []
              }

g = Graph(customDict)
print(g.checkRoute("a", "j"))  # True

################################## 2 ###################################################
"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

Example

sortedArray = [1,2,3,4,5,6,7,8,9]
minimalTree(sortedArray)
 
#Output
 
   _5__  
  /    \ 
  3    8 
 / \  / \
 2 4  7 9
/    /   
1    6 
"""


# Minimal Binary Search Tree

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimalTree(sortedArray):
    # base condition
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])

    # recursive case
    mid = len(sortedArray) // 2
    root = BSTNode(sortedArray[mid])
    root.left = minimalTree(sortedArray[:mid])
    root.right = minimalTree(sortedArray[mid + 1:])

    return root


def level_order_traversal(root_node: BSTNode):
    if not root_node:
        return

    q = []
    q.append(root_node)

    while q:
        node = q.pop(0)
        print(node.data)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = minimalTree(sortedArray)
level_order_traversal(bst)

###################### 3 ########################
#################################################
"""
Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth 
(ie , if you have a tree with depth D, you’ll have D linked lists)

"""


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    # base condition
    if tree is None:
        return 0
    # recursive case
    left = 1 + depth(tree.left)
    right = 1 + depth(tree.right)
    return max(left, right)


def treeToLinkedList(tree, custDict={}, d=None):
    queue = []
    queue.append(tree)

    while queue:
        node = queue.pop(0)
        d = depth(node)
        if d not in custDict:
            custDict[d] = LinkedList(node.val)
        else:
            custDict[d].add(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append((node.right))

    return custDict


one = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

ans = treeToLinkedList(one)

for key, value in ans.items():
    print(f"{key}: {value}")

######### 4 ############################################
########################################################
"""
Check Balanced - LeetCode 110
Implement a function to check if a binary tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
"""


# Balanced Tree

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(node: Node):
    if node is None:
        return 0
    left = 1 + height(node.left)
    right = 1 + height(node.right)

    return max(left, right)


def isBalanced(root):
    left_height = height(root.left)
    right_height = height(root.right)
    diff = left_height - right_height

    return abs(diff) <= 1


############### 5 ################################################
##################################################################

"""
Implement a function to check if a binary tree is a Binary Search Tree.
"""


# Validate BST

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def isValidBST_helper(root, min, max):
    if not root:
        return True

    if root.left:
        if min <= root.left.val <= max:
            pass
        else:
            return False

    if root.right:
        if min <= root.right.val <= max:
            pass
        else:
            return False

    return isValidBST_helper(root.left, min, max) and isValidBST_helper(root.right, min, max)


def isValidBST(root):
    left_side = isValidBST_helper(root.left, float("-inf"), root.val)
    right_side = isValidBST_helper(root.right, root.val, float("inf"))

    if not left_side or not right_side:
        return False
    else:
        if root.left.val <= root.val <= root.right.val:
            return True
        else:
            return False


root = TreeNode(51)
t1 = TreeNode(4)
t2 = TreeNode(60)
t3 = TreeNode(2)
t4 = TreeNode(3)
t5 = TreeNode(52)
t6 = TreeNode(70)
root.left = t1
root.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6

print(isValidBST(root))

################ 6 ##########################################################
#############################################################################

"""
In-order Successor in BST - LeetCode 285
Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree. 
You may assume that each node has a link to its parent.
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node


def helper_inoder_traversal(root, array):
    if root is None:
        return array
    helper_inoder_traversal(root.left, array)
    array.append(root)
    helper_inoder_traversal(root.right, array)

    return array


def inOrderSuccessor(root, n):
    array = helper_inoder_traversal(root, [])
    i = 0
    for a in array:
        if a == n:
            print(f"The successor of {n.data} is {array[i + 1].data}")
            break
        else:
            i += 1


## another option

def minValue(node):
    current = node
    while (current is not None):
        if current.left is None:
            break
        current = current.left
    return current


def inOrderSuccessor1(root, n):
    # case 1: if node has a right child, then the right value comes next for in-order traversal
    if n.right is not None:
        return minValue(n.right)

    # case 2: if node has no right child, then traverse upwards
    # traverse up the parent pointers until it finds a
    # node whose left child is also an ancestor of the given node

    p = n.parent
    while p is not None:
        if n == p.left:
            break
        n = p
        p = p.parent
    return p


bst = Node(10)
insert(bst, 100)
insert(bst, 20001)
insert(bst, 68)
insert(bst, 12)
insert(bst, 7)
insert(bst, 13908)
insert(bst, 8)
insert(bst, 14)

inOrderSuccessor(bst, bst.left.right)

temp = bst.left.right
successor = inOrderSuccessor1(root, temp)
print(successor.data)
if successor is not None:
    print("Inorder successor of %d is %d" % (temp.data, successor.data))
else:
    print("Inorder successor does not exist")


############### 7 #####################################
#######################################################


# Build Order

# projects a,b,c,d,e,f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph


def findBuildOrder(projects, dependencies):
    # This is a topological sort for a graph
    def helper(visited, stack, graph, vertex):
        visited.append(vertex)

        for edge in graph[vertex]:
            if edge not in visited:
                helper(visited, stack, graph, edge)

        stack.append(vertex)

    project_graph = createGraph(projects, dependencies)
    visited = []
    stack = []

    for vertex in project_graph:
        if vertex not in visited:
            helper(visited, stack, project_graph, vertex)

    while stack:
        print(stack.pop())


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
findBuildOrder(projects, dependencies)

##### 8 #################################
#########################################
"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 

Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
"""


# First Common Ancestor

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def get_path(n, root):
    if not root:
        return []
    if n == root:
        return [root]

    lpath = get_path(n, root.left)
    if lpath:
        return [root] + lpath

    rpath = get_path(n, root.right)
    if rpath:
        return [root] + rpath

    return []


def findFirstCommonAncestor1(n1, n2, root):
    # in the approach, store the path of each node
    # then check the last node they had in coming
    path1 = get_path(n1, root)
    path2 = get_path(n2, root)

    for i, (x, y) in enumerate(zip(path1, path2)):
        if x != y:
            return path1[i - 1]

    # if no difference is found:
    m = min(len(path1), len(path2))
    return path1[m - 1]


def is_in_tree(target, root):
    #base conditions
    if root is None:
        return False
    if root == target:
        return True

    # recursive conditions
    return (is_in_tree(target, root.left) or is_in_tree(target, root.right))


def findFirstCommonAncestor2(node1, node2, root):
    #base conditions
    if root is None:
        return None

    if root == node1 or root == node2:
        return root

    # recursive conditions
    left = findFirstCommonAncestor2(node1, node2, root.left)
    right = findFirstCommonAncestor2(node1, node2, root.right)

    if left and right:
        return root

    if left is None:
        return right

    if right is None:
        return left




root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(21)
root.left.right = Node(22)
root.right.left = Node(31)
root.right.right = Node(32)

ans = findFirstCommonAncestor1(root.right, root.right.right, root)
print("FCA = ", end="")
print(ans.value)

ans = findFirstCommonAncestor2(root.right, root.right.right, root)
print("FCA = ", end="")
print(ans.value)


