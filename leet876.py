# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        median = 0
        while curr:
            median += 1
            curr = curr.next
        median = (median // 2)
        curr = head
        for _ in range(median):
            curr = curr.next
            median -= 1
        return curr
