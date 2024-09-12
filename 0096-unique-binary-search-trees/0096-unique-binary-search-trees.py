class Solution:
    def numTrees(self, n: int) -> int:
        # dp[nodes] = dp[nodes] + dp[left] × dp[right]
        dp = [0] * (n + 1)
        # Base cases
        dp[0] = 1  # There's one empty tree
        dp[1] = 1  # There's one tree with one node

        # The outer loop goes through each possible tree size (nodes from 2 to n).
        # The inner loop goes through each possible node as the root (root from 1 to nodes).
        # The reason we start from 2 is because we already know the base cases for 0 and 1 node:
        for nodes in range(2, n + 1):
            # iterates over all possible values of root, because the root of a BST can be any node.
            for root in range(1, nodes + 1):
                left = root - 1 # number of nodes in the left subtree
                right = nodes - root # number of nodes in the right subtree
                dp[nodes] += dp[left] * dp[right]

        return dp[-1]
