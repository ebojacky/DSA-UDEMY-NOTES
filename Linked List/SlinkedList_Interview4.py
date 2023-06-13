# sum llinked list function

# note that the numbers are stored in reversed order in llist

import SingleLinkedList

LLA = SingleLinkedList.SLinkedList([7, 1, 6])
LLB = SingleLinkedList.SLinkedList([5, 9, 2])


def sum_ll(lla, llb):
    llc = SingleLinkedList.SLinkedList([])

    h1 = lla.head
    h2 = llb.head

    carry = 0

    while h1 or h2:
        res = 0
        if h1:
            res += h1.value
            h1 = h1.next
        if h2:
            res += h2.value
            h2 = h2.next

        res += carry
        llc.append(res % 10)

        carry = int(res / 10)

    return llc


sum_ll(LLA, LLB).print()


def sum_ll2(lla, llb):
    llc = SingleLinkedList.SLinkedList([])

    l1 = int("".join([n for n in lla][::-1]))
    l2 = int("".join([n for n in llb][::-1]))
    l3 = str(l1 + l2)[::-1]
    for c in l3:
        llc.append(int(c))

    return llc


sum_ll(LLA, LLB).print()
