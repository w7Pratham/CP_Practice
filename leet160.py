# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        pta = headA
        ptb = headB
        
        while pta is not ptb:
            pta = headB if pta is None else pta.next
            ptb = headA if ptb is None else ptb.next
        
        return pta
