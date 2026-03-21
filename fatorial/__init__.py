from fatorial.node import Node
from fatorial.functions import Multiply, print_list

def main():
	n = 100
	head = Node(1)
	for i in range(2, n+1):
		Multiply(head, i)

	print(f'factorial of {n}, is:')
	print_list(head)
	print()