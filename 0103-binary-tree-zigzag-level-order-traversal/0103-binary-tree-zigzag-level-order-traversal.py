# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = deque([root])
        left = False
        while q:
            qlen = len(q)
            current = []
            for i in range(qlen):
                node = q.popleft()
                current.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if left:
                current.reverse()
            left = not left
            ans.append(current)
            
        return ans