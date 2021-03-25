# Sentence Reverse
# You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

# Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

# Explain your solution and analyze its time and space complexities.

# Example:

# input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
#                 'm', 'a', 'k', 'e', 's', '  ',
#                 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

# output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
#           'm', 'a', 'k', 'e', 's', '  ',
#           'p', 'e', 'r', 'f', 'e', 'c', 't' ]

def reverseInput(array, start, end):
	while (start < end):
		tmp = array[start]
		array[start] = array[end]
		array[end] = tmp
		start += 1
		end -= 1

def reverseWord(arr):
	len_ = len(arr) - 1
	reverseInput(arr, 0, len_)

	wordStart = None
	for i in range(len_):
		if (arr[i] == ' '):
			if (wordStart != None):
				reverseInput(arr, wordStart, i - 1)
				wordStart = None
		elif (i == len_):
			if (wordStart != None):
				reverseInput(arr, wordStart, i)
		else:
			if (wordStart == None):
				wordStart = i
	return arr



arr =  ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
#print(reverseCharacter (arr, 0, len(arr) - 1))
print(reverseWord(arr))