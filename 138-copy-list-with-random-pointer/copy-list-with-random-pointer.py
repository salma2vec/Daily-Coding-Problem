class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # Create a mapping from original nodes to copied nodes
        mapping = {}
        
        # First pass: create copied nodes without random pointers
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        # Second pass: add random pointers
        current = head
        while current:
            if current.random:
                mapping[current].random = mapping[current.random]
            if current.next:
                mapping[current].next = mapping[current.next]
            current = current.next
        
        return mapping[head]

        