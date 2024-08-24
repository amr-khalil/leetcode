# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, values):
            if not node:
                return
            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)

            return values
        
        ans = []
        dfs(root, ans)
        return ans
            