# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helper function to check if two trees are identical
        def is_same_tree(node1, node2):
            # If both nodes are None, the trees are identical
            if not node1 and not node2:
                return True
            # If one node is None and the other is not, trees are not identical
            if not node1 or not node2:
                return False
            # If the values of the nodes do not match, the trees are not identical
            if node1.val != node2.val:
                return False

            return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)


        def dfs(node):
            # If the current node is None, it means we've reached the end of this path, return False
            if not node:
                return False
            
            # Check if the current subtree rooted at 'node' matches the 'subRoot'
            if is_same_tree(node, subRoot):
                return True

            # Recursively check the left and right subtrees
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)