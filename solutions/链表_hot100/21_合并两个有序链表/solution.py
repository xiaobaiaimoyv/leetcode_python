# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = list1, list2
        dummy = ListNode()
        p0 = dummy
        if not a:
            return b
        if not b:
            return a
        while a and b:
            if a.val >= b.val:
                p0.next = b
                p0 = p0.next
                b = b.next if b else None
            else:
                p0.next = a
                p0 = p0.next
                a = a.next if a else None
        if a:
            p0.next = a
        if b:
            p0.next = b
        return dummy.next


