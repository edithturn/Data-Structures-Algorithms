"""
Steps:
- Define funcion A (current_node)
	- Get current.node.left
	- Get current.node.right
	- Nothing if node is empy
	- Swap  the values
	 - Function A (current.node.left)
	 - Function A (current.node.right)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# retorna el binary tree al revez
class Solution:
    def ReverseTree(root: TreeNode):
		if root == None:
			return
		temp = 	root.leff
		root.leff = root.rigth
		root.rigth =  temp
		ReverseTree(root.leff )
		ReverseTree(root.right )



if __name__ = "__main__"
	root = TreeNode(94)
	root.left = TreeNode()
	root.right =  TreeNode()
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)
	res =  