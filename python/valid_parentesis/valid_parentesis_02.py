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


def bracketMatch(expresion):
	count = 0
	total = 0
	len_ = len(expresion) 

	for i in range(len_):
		if expresion[i]  == '(':
			count += 1
		elif (expresion[i] == ')'):
			count -= 1
		if (count < 0):
			count += 1
			total += 1
	return total + count

print(bracketMatch(")("))