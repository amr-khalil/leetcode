"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.children:
                    for c in node.children[::-1]:
                        stack.append(c)
                ans.append(node.val)
        return ans

        