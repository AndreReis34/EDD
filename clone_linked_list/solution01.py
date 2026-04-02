from clone_linked_list.conf import Node, printList

def cloneLinkedList(head):
    nodeMap = {}
    curr = head

    while curr is not None:
        nodeMap[curr] = Node(curr.data)
        curr = curr.next

    curr = head

    while curr is not None:
        newNode = nodeMap[curr]

        newNode.next = nodeMap.get(curr.next)

        newNode.random = nodeMap.get(curr.random)

        curr = curr.next

    return nodeMap.get(head)

def main01():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next
    
    # Print the original list
    print("Original linked list:")
    printList(head)
    
    clonedList = cloneLinkedList(head)
    
    print("Cloned linked list:")
    printList(clonedList)
