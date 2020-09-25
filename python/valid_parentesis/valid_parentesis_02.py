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