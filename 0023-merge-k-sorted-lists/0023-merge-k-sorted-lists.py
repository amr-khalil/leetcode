# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for head in lists:
            while head:
                nodes.append(head.val)
                head = head.next
        
        nodes.sort()
        head = point = ListNode(val=0)
        for n in nodes:
            point.next = ListNode(val=n)
            point = point.next
        return head.next