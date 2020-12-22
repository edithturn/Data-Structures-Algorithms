# [1 , -5, -6 , 3, 4, 2 ]
# 1, 2, 3,4, 5

# BigO: O(n^2)
def MaxProduct():
	s = [1 , -5, -6 , 3, 4, 2 ]
	t = ()
	_len = len(s)
	r = -99
	for i in range(_len):
		for j in range(i+1,_len):
			if (s[i] * s[j] > r):
				t = (s[i], s[j])
			r = max(r, s[i] * s[j])
	#print(t)
	#print (r)

# BigO O(n log n) | Sorting
def MaxProductTwo():
	s = [1 , -5, -20, -6 , 3, 4, 2, 8 ]
	t = sorted(s)
	if(t[0] * t[1] > t[-1] * t[-2]):
		print(t[0], t[1])
	else:
		print(t[-1], t[-2])

if __name__ == '__main__':
	MaxProductTwo()


	# 1 * -5
	# 1 * -6 
	# 1 * 3
	# 1 * 4
	# 1 *  2
	#max(4)
	# 1 and 4 = 4

	# -5 * -6 
	# -5 * 3
	# -5 * 4
	# -5 * 2
	# -5 and -6 = 30

