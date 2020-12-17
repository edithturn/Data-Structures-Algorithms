import unittest
from MinStack import MinStack

'''
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
'''

#TODO
class TestStack(unittest.TestCase): 
	stack = []
	def test_push(self):
		stack.push(-2)
		stack.push(0)
		stack.push(-3)
		stack.getMin()
		stack.pop()
		stack.top()
		self.assertTrue(stack.getMin(), )

if __name__ == '__main__':
    unittest.main()