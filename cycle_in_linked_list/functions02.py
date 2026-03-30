from cycle_in_linked_list.node import Node

def detectLoop(head):

    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow ==fast:
            return True
    return False


def main02():
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    head.next.next.next = head.next

    if detectLoop(head):
        print("true")
    else:
        print("false")
