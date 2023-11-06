# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Count the number of nodes in the linked list
        count = 1
        current = head
        while current.next:
            count += 1
            current = current.next

        # Calculate the effective rotation amount
        k = k % count
        if k == 0:
            return head

        # Find the new head and the previous node of the new head
        current = head
        for _ in range(count - k - 1):
            current = current.next
        new_head = current.next
        current.next = None

        # Connect the tail of the original list to the original head
        current = new_head
        while current.next:
            current = current.next
        current.next = head

        return new_head        