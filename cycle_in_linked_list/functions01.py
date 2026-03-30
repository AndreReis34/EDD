from cycle_in_linked_list.node import Node

def detectLoop(head):
    st = set()

    while head is not None:
        if head in st:
            return True

        st.add(head)

        head = head.next

    return False


def main01():
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    head.next.next.next = head.next

    if detectLoop(head):
        print("true")
    else:
        print("false")
