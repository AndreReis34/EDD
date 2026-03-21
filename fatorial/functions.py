from fatorial.node import Node

def Multiply(head, i):
	temp = head
	prevPtr  = head
	carry = 0 

	while temp is not None:
		prod  = temp.data * i + carry
		temp.data =  prod % 10 
		carry = prod//10
		prevPtr = temp
		temp = temp.prev

	while carry != 0:
		prevPtr.prev = Node(carry%10)
		carry = carry // 10
		prevPtr = prevPtr.prev

def print_list(head):
	if head is None:
		return

	print_list(head.prev)
	print(head.data, end="")

