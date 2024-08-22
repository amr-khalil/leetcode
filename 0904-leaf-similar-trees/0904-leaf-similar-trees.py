# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Helper function to perform a depth-first search (DFS) to collect leaf node values
        def dfs(node, leafs):
            # Base case: If the node is None, return immediately (no action needed)
            if not node:
                return
            # If the node is a leaf (no left or right child), add its value to the leaf list
            if not node.left and not node.right:
                leafs.append(node.val)
            # Recursively traverse the left and right children
            dfs(node.left, leafs)
            dfs(node.right, leafs)

        # Initialize lists to store leaf sequences for both trees
        leafs1 = []
        leafs2 = []

        # Collect the leaf sequences for both trees using DFS
        dfs(root1, leafs1)
        dfs(root2, leafs2)

        # Compare the two leaf sequences for equality
        return leafs1 == leafs2
