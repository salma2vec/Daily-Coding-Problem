class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split the linked list into two halves
        mid = slow.next
        slow.next = None

        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right  # Corrected the missing dot here
                right = right.next
            current = current.next

        current.next = left if left else right

        return dummy.next

        