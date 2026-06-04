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
	st = []
	res = []

	for c in s:
		if('a'<=c<='z')or('A'<=c<='Z')or('0'<=c<='9'):
			res.append(c)
		elif c == '(':
			st.append('(')
		elif c == ')':
			