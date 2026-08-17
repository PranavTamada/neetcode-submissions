# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxd = 0
        if root  == None:
            return 0
        def rec(root,n):
            nonlocal maxd
            if root  != None:
                n += 1 
                maxd = max(maxd,n)
                if root.left:
                    rec(root.left,n)
                if root.right:
                    rec(root.right,n)
            return
        rec(root,0)
        return maxd

        