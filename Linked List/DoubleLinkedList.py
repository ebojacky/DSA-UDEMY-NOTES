class DLinkedList:
    def __init__(self, values):
        self.head = None
        self.tail = None

        for value in values:
            self.append(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node

            node = node.next

    def __str__(self):
        str_ = []
        for node in self:
            str_.append(node.value)

        str_ = [str(item) for item in str_]
        return " <=> ".join(str_)

    class Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def append(self, value):
        new_node = DLinkedList.Node(value)

        if self.head is None:
            self.head = new_node

        if self.tail is None:
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, value, location):
        new_node = DLinkedList.Node(value)
        if location == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            inserted = False

            for index, node in enumerate(self):
                if index == location:
                    new_node.next = node
                    new_node.prev = node.prev

                    new_node.next.prev = new_node
                    new_node.prev.next = new_node

                inserted = True

            if not inserted:
                self.append(value)

    def traverse(self):
        for node in self:
            print(node.value)

    def reverse_traverse(self):
        node = self.tail

        while node:
            print(node.value)
            node = node.prev

    def search(self, value):
        for index, node in enumerate(self):
            if node.value == value:
                return True, index
        return False, -1

    def delete(self, loc):
        if loc == 0:
            if self.head is not None:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
        else:
            for index, node in enumerate(self):
                if index == loc:
                    if node == self.tail:
                        node.prev.next = None
                        self.tail = node.prev
                    else:
                        node.next.prev = node.prev
                        node.prev.next = node.next


dll = DLinkedList([111, False, ["RED", "GREEN", "BLUE"], 333])
print(dll)
dll.insert("DRACULA", 0)
print(dll)
dll.insert("MEEK", 100)
print(dll)
print("Inserting Ronaldo")
dll.insert("RONALDO", 4)
print(dll)
dll.traverse()
dll.reverse_traverse()
dll.insert("RASHFORD", 7)
print(dll)
dll.traverse()
dll.reverse_traverse()
print(dll.search(333))
print("TESTING DELETION")
print(dll)
dll.delete(0)
print(dll)
dll.traverse()
dll.reverse_traverse()
dll.delete(4)
print(dll)
dll.traverse()
dll.reverse_traverse()
dll.delete(2)
print(dll)
dll.traverse()
dll.reverse_traverse()
