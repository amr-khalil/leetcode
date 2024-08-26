# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        max_sum = 0
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        start = head
        while prev:
            curr_sum = start.val + prev.val
            max_sum = max(max_sum, curr_sum)
            prev = prev.next
            start = start.next
            
        return max_sum


