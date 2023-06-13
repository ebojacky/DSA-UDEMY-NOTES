# Animal Shelter For Dogs and Cats
from enum import Enum


class Animal(Enum):
    Dog = "DOG"
    Cat = "CAT"


class Node:
    def __init__(self, name, type_of_animal):
        self.name = name
        self.type = type_of_animal
        self.next = None


class ShelterQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        strs = ""
        for node in self:
            strs += f"({node.name},{node.type.value})--"
        strs += "None"
        return strs

    def enqueue(self, name, type_of_animal):
        new_node = Node(name, type_of_animal)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        node = self.head
        if node is not None:
            self.head = self.head.next
            return node.name, node.type.value

    def dequeue_dog(self):
        if self.head is not None:
            if self.head.type == Animal.Dog:
                return self.dequeue()
            else:
                prev = self.head
                node = self.head.next
                while node:
                    if node.type == Animal.Dog:
                        node_to_dequeue = node
                        prev.next = node.next
                        return node_to_dequeue.name, node_to_dequeue.type.value

                    prev = node
                    node = node.next

    def dequeue_cat(self):
        if self.head is not None:
            if self.head.type == Animal.Cat:
                return self.dequeue()
            else:
                prev = self.head
                node = self.head.next
                while node:
                    if node.type == Animal.Cat:
                        node_to_dequeue = node
                        prev.next = node.next
                        return node_to_dequeue.name, node_to_dequeue.type.value

                    prev = node
                    node = node.next


my_shelter = ShelterQueue()
print(my_shelter)
print(my_shelter.dequeue())
print(my_shelter.dequeue_dog())
print(my_shelter.dequeue_cat())
my_shelter.enqueue("Tom", Animal.Dog)
my_shelter.enqueue("Jerry", Animal.Cat)
my_shelter.enqueue("Sheeba", Animal.Dog)
my_shelter.enqueue("Judah", Animal.Dog)
my_shelter.enqueue("Esi", Animal.Cat)
my_shelter.enqueue("Ama", Animal.Cat)

print(my_shelter)

print(my_shelter.dequeue())
print(my_shelter)

print(my_shelter.dequeue())
print(my_shelter)

print("Dequeuing Dog")

print(my_shelter.dequeue_dog())
print(my_shelter)

print(my_shelter.dequeue_dog())
print(my_shelter)

print(my_shelter.dequeue_dog())
print(my_shelter)

print("Dequeuing Cat")

print(my_shelter.dequeue_cat())
print(my_shelter)

