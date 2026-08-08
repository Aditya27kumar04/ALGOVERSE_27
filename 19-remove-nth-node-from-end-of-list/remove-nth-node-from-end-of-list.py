# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        slow = head

        # Move fast n nodes ahead
        for i in range(n):
            fast = fast.next

        # If fast becomes None, remove the first node
        if fast is None:
            return head.next

        # Move both pointers
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the node
        slow.next = slow.next.next

        return head