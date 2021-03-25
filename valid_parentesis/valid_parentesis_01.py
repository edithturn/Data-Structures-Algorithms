# A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

# Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

# Explain the correctness of your code, and analyze its time and space complexities.

# Examples:
# input:  text = “(()”
# output: 1
# input:  text = “(())”
# output: 0
# input:  text = “())(”
# output: 2

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
