# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def rec(root):
            if not root:
                return 
            nums.append(root.val)
            if root.right:
                rec(root.right)
            if root.left:
                rec(root.left)
        rec(root)
        nums.sort()
        return nums[k-1]

        