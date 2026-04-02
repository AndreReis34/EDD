from clone_linked_list.conf import Node, printList

def cloneLinkedList(head):
	if head is None:
		return None

	curr = head
	while curr is not None:
		newNode = Node(curr.data)
		newNode.next = curr.next
		curr.next = newNode
		curr = newNode.next

	curr = head
	while curr is not None:
		if curr.random is not None:
			curr.next.random = curr.random.next
		curr = curr.next.next

	curr = head
	clonedHead = head.next
	clone = clonedHead

	while clone.next is not None:
		curr.next = curr.next.next
		clone.next = clone.next.next

		curr = curr.next
		clone = clone.next

	curr.next = None
	clone.next = None

	return clonedHead

def main02():
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