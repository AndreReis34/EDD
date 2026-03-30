from reverse_linked_list.node import Node

def reverseList(head):
    curr = head
    prev = None

    while curr is not None:
        nextNode = curr.next

        curr.next = prev

        prev = curr

        curr =  nextNode

    return prev
    

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")

        node = node.next
    print()



def main01():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)


    printList(head)
    head = reverseList(head)
    printList(head)
