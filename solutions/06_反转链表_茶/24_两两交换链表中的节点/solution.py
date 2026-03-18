# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        count = 0
        while h:
            count += 1
            h = h.next
        sb = ListNode(next=head)
        p0 = sb
        while count >= 2:
            count -= 2
            pre = None
            cur = p0.next
            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return sb.next


