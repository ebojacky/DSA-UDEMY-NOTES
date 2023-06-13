import SingleLinkedList

# nth node from last one

sll = SingleLinkedList.SLinkedList([1, 2, 4, 6, 8, 0, 8, 4, 2, 1])

pointer1 = sll.head
pointer2 = sll.head

k = 0
while pointer1:
    pointer1 = pointer1.next
    k += 1
n = 5

diff = k - n

for i in range(diff):
    pointer2 = pointer2.next

print(pointer2.value)

# another approach #

list_ = [node.value for node in sll]
print(list_[-n])
