# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next

        l, r = 0, len(values)-1
        max_sum = 0
        while l < r:
            curr_sum = values[l] + values[r]
            max_sum = max(max_sum, curr_sum)
            l += 1
            r -= 1
        
        return max_sum