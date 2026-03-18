# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sb = ListNode()
        sb.next = head
        po = sb
        for _ in range(left - 1):
            po = po.next
        pre = None
        cur = po.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        po.next.next = cur
        po.next = pre
        return sb.next

