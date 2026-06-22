def prec(c):
	if c == '^':
		return 3
	elif c == '/' or c == '*':
		return 2
	elif c == '+' or c == '-':
		return 1
	else:
		return -1


def isRightAssociative(c):
	return c == '^'

def infixToPostfix(s):
	pass