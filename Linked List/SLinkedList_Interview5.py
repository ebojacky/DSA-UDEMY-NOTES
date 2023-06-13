# find the intersection Node of 2 linked list
import random

from SingleLinkedList import SLinkedList, Node

n1 = Node(111)
n2 = Node(333)
n3 = Node(555)
n1.next = n2
n2.next = n3

node = n1
while node:
    print(node.value)
    node = node.next

ll_1 = SLinkedList([2, 3, 4, 5, 6, 7, 8])
ll_2 = SLinkedList([7, 8])

ll_1.tail.next = n1
ll_2.tail.next = n3

ll_1.print()
ll_2.print()

len1 = len(ll_1)
len2 = len(ll_2)

if len1 > len2:
    outer = ll_2
    inner = ll_1
else:
    outer = ll_1
    inner = ll_2

found = False

head1 = outer.head
while head1 and not found:
    head2 = inner.head
    while head2 and not found:
        if head1 is head2:
            print(f"Intersecting Node = {head1.value}")
            found = True

        head2 = head2.next

    head1 = head1.next


print("another approach")

diff = len1 - len2
if diff > 0:
    longer = ll_1
    shorter = ll_2
else:
    longer = ll_2
    shorter = ll_1

head_longer = longer.head
head_shorter = shorter.head

for i in range(0, diff):
    head_longer = head_longer.next

while head_longer is not head_shorter:
    head_longer = head_longer.next
    head_shorter = head_shorter.next

print(f"Intersecting Node = {head_longer.value}")




