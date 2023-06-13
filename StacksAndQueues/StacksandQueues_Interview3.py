# Implement a stack with a maximum size per substack

class ParentStack:
    def __init__(self, limit_per_substack):
        self.limit = limit_per_substack
        self.sub_stacks = []

    def __str__(self):
        strings = ""

        for list_ in self.sub_stacks:
            for item in list_:
                strings += str(item) + ","

            strings += " || "

        return strings

    def push(self, item):
        if self.sub_stacks and len(self.sub_stacks[-1]) < self.limit:
            self.sub_stacks[-1].append(item)
        else:
            self.sub_stacks.append([item])

    def pop(self):
        if self.sub_stacks[-1]:
            return self.sub_stacks[-1].pop()

    def pop_at(self, sub_stack_number):
        if self.sub_stacks[sub_stack_number]:
            return self.sub_stacks[sub_stack_number].pop()


ps = ParentStack(4)
ps.push("A")
ps.push("C")
ps.push("E")
ps.push("H")
ps.push("Q")
ps.push("Z")
ps.push("K")
print(ps.sub_stacks)
ps.pop()
print(ps.sub_stacks)
ps.pop_at(0)
print(ps.sub_stacks)
print(ps)
