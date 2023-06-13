class CDLinkedList:
    def __init__(self, nodes: list):
        self.head = None
        self.tail = None

        for node in nodes:
            self.append(node)

    def __iter__(self):
        node = self.head
        while node:
            yield node

            if node == self.tail:
                break

            node = node.next

    def __str__(self):
        values = []
        for node in self:
            values.append(node.value)

        values = [str(v) for v in values]
        return "<= " + " <==> ".join(values) + " =>"

    class Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def append(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.head.prev = new_node

        if self.tail is None:
            self.tail = self.head

        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = self.tail

    def insert(self, value, loc):
        new_node = self.Node(value)

        if loc == 0:
            if self.head is None:
                self.append(value)
            else:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
        else:
            for index, node in enumerate(self):
                if index == loc:
                    new_node.next = node
                    new_node.prev = node.prev
                    node.prev.next = new_node
                    node.prev = new_node
                    return
            self.append(value)

    def traverse(self):
        values = []
        node = self.head

        i = 0
        while node:
            values.append(node.value)
            if node == self.head and i > 1:
                break
            node = node.next
            i += 1

        values = [str(v) for v in values]
        return "Starting from HEAD back to HEAD...\n" + "<= " + " <==> ".join(values) + " =>"

    def traverse_reverse(self):
        values = []
        node = self.tail

        i = 0
        while node:
            values.append(node.value)
            if node == self.tail and i > 1:
                break
            node = node.prev
            i += 1

        values = [str(v) for v in values]
        return "Starting from TAIL back to TAIL...\n" + "<= " + " <==> ".join(values) + " =>"

    def delete(self, loc):
        if loc == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head

        else:
            for index, node in enumerate(self):
                if index == loc:
                    if node == self.tail:
                        self.tail = node.prev
                        self.tail.next = self.head
                        self.head.prev = self.tail
                    else:
                        node.next.prev = node.prev
                        node.prev.next = node.next


cdll = CDLinkedList([111, 444])
print(cdll)
print(cdll.traverse_reverse())
cdll.insert("AAA", 0)
print(cdll)
print(cdll.traverse_reverse())
cdll.insert("BBB", 4)
print(cdll)
print(cdll.traverse_reverse())
cdll.insert("CCC", 1000)
print(cdll)
print(cdll.traverse_reverse())
cdll.insert("MMM", 2)
print(cdll)
print(cdll.traverse())
print(cdll.traverse_reverse())
print("Testing Deletion")
print(cdll)
cdll.delete(5)
print(cdll)
print(cdll.traverse())
print(cdll.traverse_reverse())
