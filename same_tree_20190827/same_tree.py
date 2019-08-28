class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

tree3 = TreeNode(1)
tree3.right = TreeNode(2)

tree4 = TreeNode(1)
tree4.left = TreeNode(1)
tree4.right = TreeNode(3)

tree5 = TreeNode(1)
tree5.left = TreeNode(1)
tree5.right = TreeNode(3)

test1 = Solution()
print(test1.isSameTree(tree5,tree4))