class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdia = 0
        def r(root):
            nonlocal maxdia
            if not root:
                return 0
            maxdia = max(r(root.left) + r(root.right), maxdia)
            return 1+max(r(root.left),r(root.right))
        _ = r(root)
        return maxdia