from merge_two_linked_list.node import Node

def sortedMerge(head1: Node, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head1.next = sortedMerge(head1.next, head2)
        return head1
    else:
        head2.next = sortedMerge(head1, head2.next)
        return head2

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" => ", end="")
        node = node.next
    print()

def main02():
    head1 = Node(5)
    head1.next = Node(10)
    head1.next.next = Node(15)
    head1.next.next.next = Node(40)


    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(20)

    res = sortedMerge(head1, head2)
    printList(res)
