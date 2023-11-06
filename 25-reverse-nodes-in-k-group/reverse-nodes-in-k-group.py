# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseLinkedList(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev, current

        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        length = getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while length >= k:
            group_start = prev_group_end.next
            group_end, next_group_start = reverseLinkedList(group_start, k)
            prev_group_end.next = group_end
            group_start.next = next_group_start
            prev_group_end = group_start
            length -= k

        return dummy.next