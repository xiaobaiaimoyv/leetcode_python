# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        now = head
        while now:
            nxt = now.next
            now.next = pre
            pre = now
            now = nxt
        return pre

    def findmid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def pairSum(self, head: Optional[ListNode]) -> int:
        x = self.reverse(self.findmid(head))
        y = head
        ans = 0
        while x and y:
            ans = max(ans, x.val + y.val)
            x = x.next
            y = y.next
        return ans

        