# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = l1, l2
        carry = 0
        dummy = ListNode()
        p0 = dummy
        while x or y or carry:
            x_val = x.val if x else 0
            y_val = y.val if y else 0
            total = x_val + y_val + carry
            p0.next = ListNode(total % 10)
            carry = total // 10
            p0 = p0.next
            if x: x = x.next
            if y: y = y.next
        return dummy.next

