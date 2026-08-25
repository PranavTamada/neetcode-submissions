# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = [root.val]
        q = deque([root])
        while q:
            level = []
            length = len(q)
            for _ in range(length):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    level.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    level.append(curr.right.val)
            if level:
                output.append(level[-1])
        return output
                