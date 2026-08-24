# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def h(root):
            if not root:
                return 0
            return 1 + max( h(root.left) , h(root.right) )
        def r(root):
            if not root:
                return True
            if abs(h(root.left) - h(root.right)) > 1:
                return False
            else:
                return r(root.left) and r(root.right)
        return r(root)