# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        even = head.next
        evenHead = even # keep the even head
        
        while even and even.next:
            # Change the pointers for odd list
            odd.next = odd.next.next
            odd = odd.next

            # Change the pointers for even list
            even.next = even.next.next
            even = even.next

        # Assign even list to the end of the odd list
        odd.next = evenHead
        
        return head
        
