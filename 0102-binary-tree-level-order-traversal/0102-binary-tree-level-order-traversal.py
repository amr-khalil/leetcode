# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        ans = []
        q = deque([root])
        while q:
            qlen = len(q)
            current = []
            # loop over every row
            for _ in range(qlen):
                node = q.popleft() # get the node
                current.append(node.val) # get the value in the current
                # add all the children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # add the current
            ans.append(current)
        return ans
            