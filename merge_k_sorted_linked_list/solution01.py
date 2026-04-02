from merge_k_sorted_linked_list.conf import Node, printList

def mergeTwo(node1, node2):
    dummy = Node(-1)
    curr = dummy

    while node1 is not None and node2 is not None:
        if node1.data <= node2.data:
            curr.next = node1
            node1 = node1.next
        else:
            curr.next = node2
            node2 = node2.next

        curr = curr.next

    if node1 is not None:
        curr.next = node1
    else:
        curr.next = node2

    return dummy.next

def mergeList(arr):
    res = None

    for node in arr:
        res = mergeTwo(res, node)
    return res


def main01():
    arr = []

    node1 = Node(1)
    node1.next = Node(3)
    node1.next.next = Node(5)
    node1.next.next.next = Node(7)
    arr.append(node1)

    node2 = Node(2)
    node2.next = Node(4)
    node2.next.next = Node(6)
    node2.next.next.next = Node(8)
    arr.append(node2)

    node3 = Node(0)
    node3.next = Node(9)
    node3.next.next = Node(10)
    node3.next.next.next = Node(11)
    arr.append(node3)

    head = mergeList(arr)
    printList(head)