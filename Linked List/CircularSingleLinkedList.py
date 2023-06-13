class CircularSLinkedList:

    def __init__(self, values):
        self.head = None
        self.tail = None

        for value in values:
            self.append(value)

    def __iter__(self):
        node = self.head

        while node:
            yield node

            if node == self.tail:
                break
            node = node.next

    def __str__(self):
        string = ""
        for node in self:
            string += f"{node.value} -> "
        string += "(HEAD)"
        return string

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def append(self, value):
        new_node = self.Node(value)

        if self.head is None:
            self.head = new_node

        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.head

        else:
            new_node.next = self.head
            self.tail.next = new_node

            self.tail = new_node

    def insert(self, value, location):
        new_node = self.Node(value)

        if location == 0:
            if self.head is None:
                self.head = new_node
            if self.tail is None:
                self.tail = new_node
                self.tail.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node

        else:
            node = self.head
            index = 0
            while node:
                if index == location - 1:
                    new_node.next = node.next
                    node.next = new_node

                if node == self.tail:
                    break

                node = node.next
                index += 1

    def traverse(self):
        for node in self:
            print(node.value)

    def search(self, value):
        for index, node in enumerate(self):
            if node.value == value:
                return True, index

        return False, -1

    def delete(self, loc):
        if loc == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        else:
            prev_node = None
            for index, node in enumerate(self):

                if index == loc:
                    if node == self.tail:
                        self.tail = prev_node
                        self.tail.next = self.head
                    else:
                        prev_node.next = node.next

                prev_node = node


csll = CircularSLinkedList([1, "EBO", 1.2, False])
print(csll)
print([i.value for i in csll])
csll.insert(100, 0)
print(csll)
csll.insert(200, 4)
print(csll)
csll.insert(300, 6)
print(csll)
csll.insert(400, 5)
print(csll)
csll.insert("C500", 1)
print(csll)
csll.traverse()
csll.delete(0)
print(csll)
print(csll.head.value)
csll.delete(6)
print(csll)
print(csll.tail.value)
print(csll.tail.next.value)
csll.delete(2)
print(csll)
csll = CircularSLinkedList([1])
print(csll)
csll.delete(0)
print(csll)
csll.append("ESTEE")
print(csll)
csll.append("JOJO")
print(csll)
csll.insert("FIIFI",1)
print(csll)