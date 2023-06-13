"""
Summary of Data Structures and Algorithms in Python
===================================================
===================================================

Queue = FIFO implementation
Stack = LIFO implementation

List = Array of elements in continues memory location. Searches are faster due to indexing
Linked-List = Objects at different locations referenced with a next pointer. Makes insertions and deletions faster


Recursion
================
Recursion is a technique in which the function calls itself
Properties:
    Perform the operations several times with different inputs
    In every step, the inputs get smaller and the problem becomes smaller
    Finally, a base condition stops the recursion and the problem gets solved

Recursion is used when sub problems are same
Used in Trees and Graphs

Basic Syntax
def recursion(input):
    if exit condition:
        do something
        return something
    else recursion(new_input)

    #after exiting recursion loop
    do something
    return something

Recursion uses STACK MEMORY (push and pop)
Recursive problems can be solved with iteration but in some situation it's complex to write iterative solutions
Recursion has memory and time overheads, because some operations are repeated
Prominent in Tree traversal

The 3 Steps for writing a recursive function:
    1. The Recursive Case = The flow
    2. The Base Condition = The Exiting / Stopping Criteria
    3. The Unintentional Case = The Constraint


Tree Algorithms
=================
Binary Tree = A tree with each node having at most 2 children
Binary Search Tree = A binary Tree where smaller elements are on the left of node and larger elements are on the right of node
AVL Tree = a BST where each node is balances, ie the diff in height of the left side and right side is 1 or less
Binary Heap =  A binary tree where the node smaller that both children (min heap) or bigger than both children (max heap)
Trie = A Trie stores data in a hierarchy, a node stores non-repetitive characters


Sorting Algorithms
==================
Bubble Sort = Compares adjacent elements and swap them based on whether they are < or >
Selection Sort = Assumes the current element is min/max. Searches for min/max in rest of the array and swaps
Insertion Sort = Starting from the 2nd element, keep shifting the element to left until it is bigger that all the left-side elements
Bucket Sort = Separate elements into buckets. Sort the buckets and merge them
Merge Sort = Find the middle of the array and divide array into left and right. Call function recursively for each side until len <=1. Then compare and sort upwards and merge
Quick Sort = Choose one element as pivot. Recursively call function for array of elements < pivot and array of elements > pivot. Merge them and return
Heap Sort = Use Binary Heap Logic to sort array


Searching Algorithms
====================
Linear Search
    For both sorted and unsorted
    Iterate items one by one

Binary Search
    For sorted List
    Divide list through the middle and recursively search
    For Numbers
    Can return bool or index


Graph Algorithms
================
Graph = Non Linear Data Structure consisting of Nodes (Vertex) and Edges connecting the nodes

Simple ways to implement graphs:
    + a matrix
    + a dictionary of lists [ADJACENCY LIST]
    + class implementation: a Node or Vertex class that has attributes for weight of edge to each neighbor
        add and remove a vertex, add and remove edges functions are needed

Traversal of Graph = Visit each Vertex : BFS and DFS
    BFS = start from a node and visit all adjacent nodes (vertices) using queue approach.
            All adjacent nodes are processed before moving on
            BFS is an algorithm that traverses a graph layer by layer, exploring all the neighbors of a node before moving on to the next layer
    DFS = start from a node and visit all adjacent nodes (vertices) using stack approach
            Only the deepest adjacent node is processed, then backtracking is done when deepest node is reached.
            DFS is an algorithm that explores the graph by going as deep as possible in each branch before backtracking

    Note: BFS and DFS are similar to Level Order Traversal

Topological Traversing / Sorting of a Graph
    Traversing or Sorting a graph according to dependency.
    =A stack is used. Add the node that has no dependency to the stack. Then when all nodes are visited, then pop the stack until empty

Single Source Shortest Path Problem
    Finding the shorted path from a given Vertex to all the vertices
    Solutions are
    1. BFS -> only for non-weighted graphs
        Queue is used
        There are no weights for the edges.
    2. Dijkstra's Algorithm
        Heap is used.
        For this algorithm, adjacency list ( dictionary  of list of edges for each vertex) may be used but with an extra variable for weight
        You may choose to create a different class of Nodes (Vertices) and Edges that takes into consideration the weight of each edge
        The main feature of this algorithm is that it uses heap to find the min distance node in the queue and pursue that path first
        But this algorithm doesn't work for negative weights. Use Bellman Ford for that.
    3. Bellman Ford
        Does not use heap
        Uses a number of iterations
        Detects Negative Paths
    4. Floyd Warshall
        Uses an adjacency matrix (not adjacency list) to find all path shorted path
        But doesn't detect negative cycle

    If there are n nodes: solving the ssspp from node x to rest of the nodes requires n-1 iterations

All Pairs Shortest Path Problem
    In this case, use each node as an input for SSSPP

Minimum Spanning Tree
For processing weighted undirected graph with the intention of finding the total minimum cost of visiting each
vertex in graph. Does not include a cycle
This uses greedy algorithm approach
    Kruskal's Algorithm
        find the minimum edge.
        find the next minimum edge that doesnt create a cycle
        Continue until completed
    Prim's Algorithm
        Start from any vertex, set weight to 0 and all others to infinity.
        Choose the min edge of all the adjacent vertexes of the current edge so long as it doesn't create a cycle
        Repeat for next vertex of the chosen edge until completed



Greedy Algorithms
=================
In each step or iteration, select the best option available.
This is the foundation of greedy algorithms.
Builds the solution piece by piece with the best option available in each iteration
Its find the best local optimum solution at each step
Take the best local solution, freeze it, and continue and add up local solutions to get global solution
Examples are Insertion Sort, Selection Sort, Topological Sort, Kruskal's and Prim's Algorithms for MST


Divide and Conquer Algorithms:
=============================
Uses Recursive Approach
Recursively breaking down a problem into sub problems of similar type, until they become simple enough
to be solved directly.
    Optimal Sub-structure Property
    Examples:
        Merge Sort
        Quick Sort
        Fibonacci
        Number Factor Problem
        House Rubber Problem


Dynamic Programming
===========================
Use the results of sub-problems to solve overall problem
This is the optimisation of divide and conquer algorithm
Save the answer of sub-problems and reuse it instead of solving them all over again
    1. Optimal Sub structure property
    2. OverLapping Sub-problem property - Solving the same sub-problem many times (like in fibonacci)

Memoization [The technique of storing the results of already solved sub-problems]. Recursion is used
    Start from the top and solve the problem downwards. Solve the top problem first. Move to next.
    When the downwards problems are solved, we come back up and solve the main problem.

Tabulation [Using a table to solve the problem]. Recursion is not used
    Bottom problems are solved first, then the original problem is solved

In general, memoization is more suitable for problems that can be solved recursively,
while tabulation is more suitable for problems that can be solved iteratively
Dynamic Programming normally finds the optimum solution


BackTracking
===========================
Relies on Recursion
Uses Brute Force Approach to find all possible solutions
- Decision Problems
- Optimisation Problems
- Enumeration Problems

Uses Space State Tree or Potential Search Tree
Backtracking uses depth first search
Bruce force uses breath search first
Back tracking is faster than Brute Force


Recipe for Solving Problems:
===========================
Algorithm = a set of steps to accomplish a task
    1. Understand the problem
        Ask questions. Seek clarification
        Can you restate the problem in your own words?
        What are the inputs, what are the outputs?
        Can the outputs be determined by the inputs?
        How to label the data and functions that come with the problem?

    2. Explore with examples
        simple examples with inputs and outputs
        what are the use cases?
        complex examples, especially the ones on the boarders
        empty inputs? invalid inputs?

    3. Break it down.
        What are the basic components of the solution?
        Don't start by writing code. Get the algorithm first
        You can use comments to break down the steps.
        You cant solve complex problems without writing your steps
        Even if you don't finish, the interviewer sees you know what you are doing

    4. Solve or simplify the problem
        solve the problem if its simple enough to solved
        if not, try breaking it down again
        To simplify a problem
            Identify the Core difficulty
            Temporarily ignore that difficulty
            Write a simplified solution
            Then incorporate the difficulty

    5. Look back and refactor
        This helps to improve the code
            Make the code more efficient in terms of time and space
            Make the code more readable
            Ask for feedback form interviewer

=====================================================================
====== END OF UDEMY COURSE =================================================


Naming Conventions In Programming
=========================

PascalCase
    FirstName
    LastName

camelCase
    firstName
    lastName

snake_case
    first_name
    last_name

kebab-case
    first-name
    last-name


Summary of Problem-Solving Approach in Programming
==================================================

Brute Force Approach:
---------------------
    This is the most straightforward algorithmic approach in which the problem is solved by exhaustively
searching through all possible solutions. It is usually inefficient and not suitable for large datasets,
but it is useful for smaller problems. This approach is commonly used when the problem is simple, and the
input size is small.

Divide and Conquer Approach:
----------------------------
    The divide and conquer algorithmic approach is a recursive method of problem-solving that breaks a problem
into smaller sub-problems, solves them separately, and then combines the solutions to the sub-problems to
get the final solution. This approach is commonly used in problems like sorting, searching, and other
related algorithms.

Dynamic Programming Approach:
-----------------------------
    The dynamic programming approach is a problem-solving technique that solves complex problems by breaking
them down into smaller sub-problems, storing the results of each sub-problem, and reusing the results to
solve larger sub-problems. This approach is useful in problems like finding the shortest path in a graph,
finding the longest common subsequence in two strings, etc.

Greedy Approach:
----------------
    The greedy algorithmic approach is a technique that solves problems by making the locally optimal choice
at each step of the algorithm, with the hope of finding a global optimum solution. This approach is useful
in problems like finding the shortest path in a weighted graph, scheduling tasks, etc.

Backtracking Approach:
----------------------
    The backtracking algorithmic approach is a technique for solving problems by systematically trying
out all possible solutions until the correct one is found. This approach is useful in problems like
finding all possible paths in a maze, solving Sudoku puzzles, etc.

Randomized Approach:
--------------------
    The randomized algorithmic approach is a technique that uses randomness to solve problems.
This approach is useful in problems like finding the median of a large dataset, generating random
numbers, etc.


CHEAT SHEET
=======================
=======================

Algorithmic Approach:

Brute Force:
    When the problem size is small and the input set is not very large.
    When the problem requires trying all possible combinations or permutations.
    When no efficient algorithm exists for the problem.
Divide and Conquer:
    When the problem can be divided into smaller sub-problems.
    When the solutions to sub-problems can be combined to solve the main problem.
    When the problem has overlapping sub-problems.
Dynamic Programming:
    When the problem can be divided into smaller sub-problems.
    When the solutions to sub-problems can be combined to solve the main problem.
    When the same sub-problems are being solved repeatedly.
Greedy:
    When the problem has optimal substructure.
    When a greedy choice can lead to the globally optimal solution.
    When the problem can be solved by making a series of locally optimal choices.
Backtracking:
    When the problem requires exploring all possible solutions.
    When the problem can be represented as a search tree.
    When the problem has a constraint that can be used to eliminate large portions of the search space.

Data Structure:

List:
    When the order of elements matters.
    When the elements need to be modified or reordered.
    When duplicate elements are allowed.
Tuple:
    When the order of elements matters.
    When the elements need to be accessed but not modified.
    When duplicate elements are allowed.
Set:
    When the order of elements does not matter.
    When duplicate elements are not allowed.
    When the set operations (union, intersection, difference) are needed.
Dictionary:
    When the data is stored as key-value pairs.
    When the data needs to be accessed by its key.
    When the data needs to be modified or reordered.
Linked List:
    When dynamic memory allocation is needed.
    When the order of elements matters.
    When elements need to be inserted or removed efficiently.
Stack:
    When the last item added is the first item removed (LIFO).
    When the order of items matters.
    When the item at the top of the stack needs to be accessed quickly.
Queue:
    When the first item added is the first item removed (FIFO).
    When the order of items matters.
    When items need to be added or removed efficiently.
Tree:
    When the data has a hierarchical structure.
    When each node can have zero or more child nodes.
    When there is a single root node.
Graph:
    When the data has a complex structure.
    When nodes can be connected to multiple other nodes.
    When there can be cycles in the graph.

============================================================================

Here are some tips and strategies for solving common Data Structures and Algorithm questions in Python:

Arrays and Lists:

Know how to traverse arrays and lists efficiently.
Understand how to use pointers to manipulate arrays and lists.
Be familiar with built-in functions for arrays and lists in Python, such as len(), append(), and pop().


Strings:

Know how to manipulate strings in Python, such as slicing, concatenation, and reversing.
Understand how to use regular expressions to search for patterns in strings.
Be familiar with built-in functions for strings in Python, such as split(), join(), and replace().


Hash Tables:

Understand how to use hash tables to store and retrieve data efficiently.
Be familiar with built-in data structures in Python for implementing hash tables, such as dict().


Trees:

Understand the basic properties of trees, such as nodes, edges, and leaves.
Be familiar with common tree traversal algorithms, such as in-order, pre-order, and post-order traversal.
Know how to implement trees in Python using classes and recursion.


Graphs:

Understand the basic properties of graphs, such as vertices and edges.
Be familiar with common graph traversal algorithms, such as depth-first search (DFS) and breadth-first search (BFS).
Know how to implement graphs in Python using classes and dictionaries.


Sorting and Searching:

Understand common sorting algorithms, such as bubble sort, insertion sort, merge sort, and quicksort.
Be familiar with built-in sorting functions in Python, such as sorted() and list.sort().
Understand common searching algorithms, such as binary search.


Dynamic Programming:

Understand the basic concept of dynamic programming, which involves breaking down complex problems into smaller subproblems.
Be familiar with common dynamic programming techniques, such as memoization and tabulation.
Know how to implement dynamic programming algorithms in Python.


Miscellaneous:

Be familiar with other common algorithms and data structures, such as stacks, queues, heaps, and linked lists.
Know how to analyze the time and space complexity of algorithms using Big O notation.
Remember, the key to solving Data Structures and Algorithm questions is to practice regularly and develop a problem-solving mindset.

"""
