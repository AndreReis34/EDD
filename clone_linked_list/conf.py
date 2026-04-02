class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.random = None

def printList(node):
	curr = node

	while curr is not None:
		print(f'{curr.data}(', end="")
		if curr.random:
			print(f'{curr.random.data})', end="")
		else:
			print('null)', end="")

		if curr.next is not None:
			print(" => ", end="")

		curr = curr.next
	print()