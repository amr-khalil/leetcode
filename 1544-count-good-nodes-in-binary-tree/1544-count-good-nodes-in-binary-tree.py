# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            # If the node is None, return 0 as there are no nodes to consider
            if not node:
                return 0
            
            # A node is "good" if its value is greater than or equal to the max value seen so far
            is_good = node.val >= max_val
            count = 1 if is_good else 0

            # Update the max value for the path
            max_val = max(max_val, node.val)

            # Recursively check left and right children, accumulating the count of good nodes
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count
        
        # Start DFS with the root and its value as the initial max value
        return dfs(root, root.val)
            