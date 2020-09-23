#Simple Balanced Parentheses
# Output: Balanced

# Example balanced
# (()()()())
# (((())))
# (()((())()))

# Example not balanced
# ((((((())
# ()))
# (()()(()
from pythonds.basic import Stack

def checkBalanced(expresion):
	index = 0
	balanced = True
	s = Stack()

	while index < len(expresion) and balanced:
		simbol = expresion[index]
		if simbol == '(':
			s.push(simbol)
		else:
			if s.isEmpty():
				balanced == False
			else:
				s.pop()
		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

print (checkBalanced('((()))()'))
print (checkBalanced('(()'))
