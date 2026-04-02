class Node(object):
	def __init__(self, newData):
		self.data = newData
		self.next = None

def printList(node):
	while node is not None:
		if node.next is not None:
			print(f'{node.data}', end=" => ")
		else:
			print(f'{node.data}')
		node = node.next

	print()


		