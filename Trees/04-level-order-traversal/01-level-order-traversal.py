class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionIterative:
    def levelOrder(self, root: Node):
        if root is None:
            return []
        queue = [root]
        nex_queue = []
        level =[]
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    nex_queue.append(root.left)
                if root.right is not None:
                    nex_queue.append(root.right)
            result.append(level)
            level = []
            queue = nex_queue
            nex_queue = []
        return result

node = Node(3)
node.left = Node(9)
node.right = Node(20)
node.right.left = Node(15)
node.right.right = Node(7)

#input root = [3,9,20,null,null,15,7]

#   3
#  / \
# 9   20
#    /  \
#   15   7

print(SolutionIterative().levelOrder(node))
        