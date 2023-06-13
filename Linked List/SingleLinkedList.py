class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:

    def __init__(self, my_list=None):
        self.head = None
        self.tail = None

        if my_list:

            for item in my_list:
                self.append(item)

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def __len__(self):
        lenn = 0
        node = self.head

        while node:
            lenn += 1
            node = node.next
        return lenn

    def print(self):
        node = self.head
        string = ""

        while node:
            string += f"{node.value} -> "
            node = node.next

        print(string + "None")

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node

        if self.tail is None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, item, loc):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        elif loc == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            for index, node in enumerate(self):
                if index == loc - 1:
                    new_node.next = node.next
                    node.next = new_node

    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def extend(self, list_):
        for item in list_:
            self.append(item)

    def search(self, value):
        for index, node in enumerate(self):
            if node.value == value:
                return True, index

        return False, -1

    def delete_by_location(self, loc):
        if loc == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        else:
            prev = None
            for index, node in enumerate(self):
                if index == loc:
                    if node == self.tail:
                        prev.next = None
                        self.tail = prev
                    else:
                        prev.next = node.next

                prev = node

    def delete_by_value(self, value):
        prev_node = None
        for current_node in self:
            if current_node:

                if current_node == self.head:
                    if current_node.value == value:
                        if self.head == self.tail:
                            self.head = self.tail = None
                        else:
                            self.head = current_node.next

                elif current_node == self.tail:
                    if current_node.value == value:
                        prev_node.next = None
                        self.tail = prev_node

                else:
                    if current_node.value == value:
                        prev_node.next = current_node.next

            prev_node = current_node


"""
my_ll = SLinkedList([])
my_ll.print()
my_ll = SLinkedList()
my_ll.print()
my_ll = SLinkedList("")
my_ll.print()
my_ll = SLinkedList("EBO")
my_ll.print()
my_ll = SLinkedList([11, 12, 113, 14, 15, 16])
my_ll.print()
my_ll.append(["EBO.J", 123])
my_ll.print()
my_ll.insert("JACKSON", 2)
my_ll.print()
my_ll.insert(666, -3)
my_ll.print()
my_ll.insert(777, 100)
my_ll.print()
my_ll.insert(888, 1)
my_ll.print()
my_ll.traverse()
my_ll.append("God is good")
my_ll.print()
print(my_ll.search("EBO"))
print(my_ll.search("JACKSON"))
print(f"tail {my_ll.tail.value}")

print("Testing deletion by location")
my_ll = SLinkedList([11, 12, 113, 14, 15, 16])
my_ll.print()
my_ll.delete_by_location(5)
my_ll.print()
print(f"tail {my_ll.tail.value}")
print(f"head {my_ll.head.value}")
my_ll.delete_by_location(0)
my_ll.print()
print(f"head {my_ll.head.value}")
my_ll.delete_by_location(2)
my_ll.print()

print("Testing deletion by value")
my_ll = SLinkedList([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("Testing deletion NOT EXIST")
my_ll.delete_by_value(9999)
my_ll.print()

print("Testing deletion TAIL")
my_ll.delete_by_value(0)
my_ll.print()
print(my_ll.tail.value)

print("Testing deletion HEAD")
my_ll.delete_by_value(1)
my_ll.print()
print(my_ll.head.value)

print("Testing deletion EXIST")
my_ll.delete_by_value(2)
my_ll.print()"""
