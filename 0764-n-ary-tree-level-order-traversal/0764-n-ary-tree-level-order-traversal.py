"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            qlen = len(q)
            curr = []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    if node.children:
                        for c in node.children:
                            q.append(c)
                    curr.append(node.val)
            ans.append(curr)
        return ans