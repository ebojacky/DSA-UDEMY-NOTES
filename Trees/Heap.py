from enum import Enum


class HeapType(Enum):
    MIN = 0
    MAX = 1


class BinaryHeap:
    def __init__(self, size, type: HeapType):
        self.max_size = size + 1
        self.items = self.max_size * [None]
        self.heap_size = 0
        self.type = type

    def peek(self):
        return self.items[1]

    def size(self):
        return self.heap_size

    def level_order_traversal(self):
        for index, item in enumerate(self.items):
            if 0 < index < self.heap_size +1:
                print(item)

    def heapify(self, index):
        parent = int (index/2)
        if parent < 1:
            return
        if self.type == HeapType.MIN:
            if self.items[index] < self.items[parent]:
                temp = self.items[parent]
                self.items[parent] = self.items[index]
                self.items[index] = temp
                self.heapify(parent)
        if self.type == HeapType.MAX:
            if self.items[index] > self.items[parent]:
                temp = self.items[parent]
                self.items[parent] = self.items[index]
                self.items[index] = temp
                self.heapify(parent)

    def insert(self, value):
        if self.heap_size < self.max_size:
            self.items[self.heap_size + 1] = value
            self.heapify(self.heap_size + 1)
            self.heap_size += 1

    def heapify_after_extraction(self, index):
        if self.items[index] is None:
            return

        if (2 * index) > self.heap_size:
            return

        left_child = self.items[2 * index]
        right_child = self.items[2 * index + 1]

        if self.type == HeapType.MIN:
            if self.items[index] > left_child or self.items[index] > right_child:
                if left_child > right_child:
                    temp = self.items[index]
                    self.items[index] = right_child
                    self.items[2 * index + 1] = temp
                    self.heapify_after_extraction(2 * index + 1)
                else:
                    temp = self.items[index]
                    self.items[index] = left_child
                    self.items[2 * index] = temp
                    self.heapify_after_extraction(2 * index)

        if self.type == HeapType.MAX:
            if self.items[index] < left_child or self.items[index] < right_child:
                if left_child < right_child:
                    temp = self.items[index]
                    self.items[index] = right_child
                    self.items[2 * index + 1] = temp
                    self.heapify_after_extraction(2 * index + 1)
                else:
                    temp = self.items[index]
                    self.items[index] = left_child
                    self.items[2 * index] = temp
                    self.heapify_after_extraction(2 * index)


    def extract(self):
        first = self.items[1]

        self.items[1] = self.items[self.heap_size]
        self.items[self.heap_size] = None
        self.heap_size -= 1

        self.heapify_after_extraction(1)
        return first


my_heap = BinaryHeap(8, HeapType.MIN)
print("---")
my_heap.level_order_traversal()
my_heap.insert(5)
my_heap.insert(10)
print("---")
my_heap.level_order_traversal()
my_heap.insert(2)
my_heap.insert(1)
print("---")
my_heap.level_order_traversal()
my_heap.insert(100)
print("---")
my_heap.level_order_traversal()
my_heap.insert(200)
print("---")
my_heap.level_order_traversal()
print("---")
print(my_heap.extract())
print("--after extraction-")
my_heap.level_order_traversal()
print("---")
print(my_heap.extract())
print("--after extraction-")
my_heap.level_order_traversal()

