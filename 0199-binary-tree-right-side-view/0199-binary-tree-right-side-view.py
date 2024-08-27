# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans = []
        q = deque([root])
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                # If it's the last node in the current level, add to right side view
                if i == qlen-1:
                    ans.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans