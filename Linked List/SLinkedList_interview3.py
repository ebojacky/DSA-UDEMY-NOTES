import SingleLinkedList


# partition sll according to value x
def partition(sll, x):
    a = SingleLinkedList.SLinkedList([])
    b = SingleLinkedList.SLinkedList([])

    for node in sll:
        if node.value < x:
            a.append(node.value)
        else:
            b.append(node.value)

    return a, b


sl_list = SingleLinkedList.SLinkedList([1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])

i, j = partition(sl_list, 4)

i.print()
j.print()


# another approach 2
def partition2(sll, x):
    a = SingleLinkedList.SLinkedList([])
    b = SingleLinkedList.SLinkedList([])

    node = sll.head
    while node:
        if node.value < x:
            a.append(node.value)
        else:
            b.append(node.value)

        node = node.next

    return a, b


sl_list = SingleLinkedList.SLinkedList([1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])

i, j = partition2(sl_list, 4)

i.print()
j.print()


# another approach 3
def partition3(sll, x):
    sll2 = SingleLinkedList.SLinkedList([])

    node = sll.head
    while node:
        if node.value < x:
            sll2.insert(node.value, 0)
        else:
            sll2.append(node.value)

        node = node.next

    return sll2


sl_list = SingleLinkedList.SLinkedList([1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])

x = partition3(sl_list, 4)

x.print()


# another approach 4 -- without creating new linked list --- moving to head
def partition3(sll, y):
    prev = sll.head
    node = prev.next
    while node:

        if node.value < y:  # move to head

            if node == sll.tail:
                sll.tail = prev

            prev.next = node.next
            node.next = sll.head
            sll.head = node
            node = prev.next

        else:
            prev = node
            node = node.next


sl_list = SingleLinkedList.SLinkedList([0, 1, 5, 6, 7, 9, 1, 2, 0])
""" 1 -> 8 -> 1"""
print("final approach")
partition3(sl_list, 5)

sl_list.print()
print(sl_list.head.value)
print(sl_list.tail.value)


# another approach 5 -- without creating new linked list
def partition3(ll, y):
    curr_node = ll.head
    ll.tail = ll.head

    while curr_node:
        next_node = curr_node.next

        if curr_node.value < y:  # move to head
            curr_node.next = ll.head
            ll.head = curr_node

        else:  # move to tail
            curr_node.next = None
            ll.tail.next = curr_node
            ll.tail = curr_node

        curr_node = next_node


sl_list = SingleLinkedList.SLinkedList([7, 8, 1, 6, 0, 1, 2])

print("final approach 2")
partition3(sl_list, 5)

sl_list.print()
print(sl_list.head.value)
print(sl_list.tail.value)
