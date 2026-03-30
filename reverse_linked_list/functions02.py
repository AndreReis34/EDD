from reverse_linked_list.node import Node

# def reverseList(head):
#     if head is None or head.next is None:
#         return head

#     rest = reverseList(head.next)

#     head.next.next = head

#     head.next = None

#     return rest 

def reverseList(head):
    stack = []

    temp = head

    while temp.next is not None:
        stack.append(temp)
        temp = temp.next

    head = temp

    while stack:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None

    return head


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node  = node.next
    print()


def insertionNode(arr, head):
    temp = head
    # head = temp
    for i in arr:
        temp.next = Node(i)
        temp = temp.next

    temp.next = None 
    return head


def main02():
    head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)

    arr = [2, 3, 4, 5]
    head = insertionNode(arr, head)

    printList(head)
    head = reverseList(head)
    printList(head)
