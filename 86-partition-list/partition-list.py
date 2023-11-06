# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        current_less = less_head
        current_greater = greater_head

        current = head

        while current:
            if current.val < x:
                current_less.next = current
                current_less = current_less.next
            else:
                current_greater.next = current
                current_greater = current_greater.next
            current = current.next

        # Connect the two partitions
        current_less.next = greater_head.next
        current_greater.next = None

        return less_head.next        