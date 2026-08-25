# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = [[root.val]]
        q = deque([root])
        out = []
        while q:
            length = len(q)
            out = []
            for _ in range(length):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    out.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    out.append(curr.right.val)
            output.append(out)
        _ = output.pop()
        return output
            