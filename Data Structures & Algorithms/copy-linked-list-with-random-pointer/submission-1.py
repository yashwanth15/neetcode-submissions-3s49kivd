"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(1) space solution
        cur=head
        # 1) Interleave cloned nodes
        while cur:
            nxt=cur.next
            copy=Node(cur.val)
            cur.next=copy
            copy.next=nxt
            cur=nxt
        
        # 2) Assign random pointers for copies
        cur=head
        while cur:
            copy = cur.next
            if cur.random:
                copy.random = cur.random.next
            cur=copy.next
        
        # 3) Split the lists
        dummy=Node(0)
        copy_cur=dummy
        cur=head
        while cur:
            copy=cur.next
            nxt=copy.next

            copy_cur.next=copy
            copy_cur=copy

            cur.next=nxt
            cur=nxt
        return dummy.next


