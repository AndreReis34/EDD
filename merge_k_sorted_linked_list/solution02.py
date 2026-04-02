from merge_k_sorted_linked_list.conf import Node, printList

def getMinNode(arr):
    mini = None 
    index = -1

    for i in range(len(arr)):
        if arr[i] is None:
            continue

        if mini is None or arr[i].data < mini.data:
            index = i 
            mini = arr[i]

        
    if index != -1:
        arr[index] = arr[index].next

    return mini

def mergeKLists(arr):
    dummy = Node(-1)
    tail = dummy

    mini = getMinNode(arr)

    while mini:
        tail.next = mini
        tail = mini

        mini = getMinNode(arr)

    return dummy.next

def main02():
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
