# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num, values):
            if not node:
                return
            
            curr_num = num * 10 + node.val
            
            if not node.left and not node.right:
                values.append(curr_num)
            
            dfs(node.left, curr_num, values)
            dfs(node.right, curr_num, values)
            return sum(values)

        return dfs(node=root, num=0, values=[])