# Remove Duplicates from linked list #
import SingleLinkedList

sll = SingleLinkedList.SLinkedList([1, 2, 3, 1, 2, 3, 4, 5])
sll.print()
sll_set = set([node.value for node in sll])
new_sll = SingleLinkedList.SLinkedList(list(sll_set))
new_sll.print()

print(" # alternative approach # ")
sll = SingleLinkedList.SLinkedList([5, 5, 3, 5])
sll.print()

node = sll.head
temp_set = {node.value}

while node.next:
    if node.next.value in temp_set:
        node.next = node.next.next
    else:
        temp_set.add(node.next.value)
        node = node.next

sll.print()

print(" # alternative approach 2 # ")
sll = SingleLinkedList.SLinkedList([5, 5, 3, 5, 1, 3, 3, 3, 3])
sll.print()

node = sll.head

while node:
    looping_node = node
    while looping_node.next:
        if looping_node.next.value == node.value:
            looping_node.next = looping_node.next.next
        else:
            looping_node = looping_node.next
    node = node.next

sll.print()
