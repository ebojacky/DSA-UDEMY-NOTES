# Show how you can use a single List to implement multiple stacks

class MultiStack:
    def __init__(self, no_of_stacks, size_per_stack):
        self.no_of_stacks = no_of_stacks
        self.size_per_stack = size_per_stack
        self.sizes_of_stacks = [0] * self.no_of_stacks
        self.list_of_items = [None] * self.no_of_stacks * self.size_per_stack

    def is_full(self, stack_number):
        if self.sizes_of_stacks[stack_number] == self.size_per_stack - 1:
            return True
        else:
            return False

    def is_empty(self, stack_number):
        if self.sizes_of_stacks[stack_number] == 0:
            return True
        else:
            return False

    def available_index(self, stack_number):
        return self.no_of_stacks * stack_number + self.sizes_of_stacks[stack_number]

    def push(self, stack_number, item):
        if not self.is_full(stack_number):
            self.list_of_items[self.available_index(stack_number)] = item
            self.sizes_of_stacks[stack_number] += 1

    def pop(self, stack_number):
        if not self.is_empty(stack_number):
            item = self.list_of_items[self.available_index(stack_number) - 1]

            self.list_of_items[self.available_index(stack_number) - 1] = None
            self.sizes_of_stacks[stack_number] -= 1

            return item

    def peek(self, stack_number):
        if not self.is_empty(stack_number):
            return self.list_of_items[self.available_index(stack_number) - 1]

    def print(self):
        for item in ms.list_of_items:
            print(item, end=":")
        print(" ")


ms = MultiStack(3, 4)
print("Push 3 items into Stack Number 2")
ms.push(2, "XYZ")
ms.push(2, "Mango")
ms.push(2, 123)
print("Print All Stacks")
ms.print()
print("Pop Stack Number 2")
print(ms.pop(2))
print("Print All Stacks")
ms.print()
ms.push(2, 125)
ms.print()
ms.push(2, 127)
ms.print()
ms.push(2, 128)
ms.print()
ms.push(2, "ABC")
ms.print()