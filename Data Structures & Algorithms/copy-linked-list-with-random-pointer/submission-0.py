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
        map = {}
        cur= head
        # create a map old node -> new node
        while cur:
            map[cur]=Node(cur.val)
            cur=cur.next
        
        # now map next and random nodes for the copy nodes
        cur=head
        while cur:
            map[cur].next = map.get(cur.next)
            map[cur].random = map.get(cur.random)
            cur=cur.next
            
        return map.get(head)