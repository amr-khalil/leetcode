# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, current_sum):
            nonlocal ans
            if not node:
                return 0

            current_sum += node.val
            diff = current_sum - targetSum
            if diff in prefix_sums:
                ans += prefix_sums[diff]
            
            # Update the prefix sums with the current sum
            prefix_sums[current_sum] += 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            prefix_sums[current_sum] -= 1
        
        # Using defaultdict to handle prefix sums
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        current_sum = 0
        ans = 0
        dfs(root, current_sum)
        return ans