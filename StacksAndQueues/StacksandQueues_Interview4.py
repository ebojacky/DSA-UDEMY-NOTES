# implement a queue with 2 stacks

class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def __str__(self):
        return "--".join([str(item) for item in self.in_stack])

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        self.out_stack = self.in_stack[::-1]
        value = self.out_stack.pop()
        self.in_stack = self.out_stack[::-1]

        return value


q = Queue()
q.enqueue(5)
q.enqueue(15)
q.enqueue(30)
q.enqueue(45)
print(q)
print(q.dequeue())
print(q)

# another approach
print("Another Appoach")


class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def pop(self):
        if self.items:
            return self.items.pop()

    def push(self, item):
        self.items.append(item)


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def __str__(self):
        return "-".join([str(items) for items in self.in_stack.items])

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        while len(self.in_stack) > 0:
            self.out_stack.push(self.in_stack.pop())

        value = self.out_stack.pop()

        while len(self.out_stack) > 0:
            self.in_stack.push(self.out_stack.pop())

        return value


q = Queue()
q.enqueue(5)
q.enqueue(15)
q.enqueue(30)
q.enqueue(45)
print(q)
print(q.dequeue())
print(q)
