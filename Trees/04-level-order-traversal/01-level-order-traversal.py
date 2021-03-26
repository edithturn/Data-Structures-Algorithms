class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Node):
        return 1



node = Node(3)
node.right = Node(9)
node.left = Node(20)
node.left.right = Node(15)
node.left.left = Node(7)

#input root = [3,9,20,null,null,15,7]

#   3
#  / \
# 9   20
#    /  \
#   15   7

print(Solution().levelOrder(node))
        