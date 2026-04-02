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

def mergeListsRecur(i, j, arr):
    if i == j:
        return arr[i]

    mid = i + (j -i) // 2

    head1 = mergeListsRecur(i, mid, arr)

    head2 = mergeListsRecur(mid+1, j, arr)

    head = mergeTwo(head1, head2)

    return head

def mergeKLists(arr):
    if len(arr)  == 0:
        return None

    return mergeListsRecur(0, len(arr)-1, arr)

def main03():
    arr = [None] * 3

    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)

    head = mergeKLists(arr)

    printList(head)


