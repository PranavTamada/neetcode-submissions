# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = []
        maxi = float("-inf")
        def r(root,maxi):
            nonlocal output
            if root.val >= maxi:
                output.append(root.val)
            maxi = max(maxi,root.val)
            if root.left:
                r(root.left,maxi)
            if root.right:
                r(root.right,maxi)
        r(root,maxi)
        return len(output)

        