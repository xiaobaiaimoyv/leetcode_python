# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(next = list1)
        left = dummy
        for _ in range(a):
            left = left.next
        right = dummy
        for _ in range(b + 2):
            right = right.next
        last = list2
        while last.next:
            last = last.next
        left.next = list2
        last.next = right
        return dummy.next


        