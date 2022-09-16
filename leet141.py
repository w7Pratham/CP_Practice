# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # try:
        #     nnext = head
        #     tnext = head.next
        #     while nnext is not tnext:
        #         nnext = nnext.next
        #         tnext = tnext.next.next
        #     return 1
        # except:
        #     return 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return 1
        return 0
