# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Advance the first pointer by n+1 positions
        for i in range(n+1):
            first = first.next

        # Move the first pointer to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next        