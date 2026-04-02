# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1) find the k-th node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes for a full group

            group_next = kth.next  # node after the group

            # 2) reverse the group
            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 3) reconnect
            old_group_start = group_prev.next
            group_prev.next = kth
            group_prev = old_group_start