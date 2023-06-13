# code a stack with minimum function at o(1) complexity

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.min = None

    def __iter__(self):
        node = self.top
        while node:
            yield node
            node = node.next

    def __str__(self):
        list_ = []
        for node in self:
            list_.append(str(node.value))
        return "--".join(list_)

    def push(self, value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
            self.min = self.top
        else:
            new_node.next = self.top
            self.top = new_node

            if new_node.value < self.min.value:
                new_min = Node(value)
                new_min.next = self.min
                self.min = new_min

    def pop(self):
        if self.top is not None:
            value = self.top.value

            if self.top.value == self.min.value:
                self.min = self.min.next

            self.top = self.top.next
            return value

    def minimum(self):
        if self.min is not None:
            return self.min.value


my_stack = Stack()
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.push(2)
my_stack.push(10)
print(my_stack)

print(my_stack.pop())
print(my_stack.min.value)
print(my_stack)

print(my_stack.pop())
print(my_stack.min.value)
print(my_stack)
