#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        p = dummy = ListNode(None)
        dummy.next = head
        p = head
        while p:
            if p.val == p.next.val:
                p.next = p.next.next
                p = p.next
            else:
                p = p.next
        return dummy.next

a = ListNode(1)
head = a
for i in [1,2,3,3]:
    head.next = ListNode(i)
    head = head.next

sol = Solution()
b = sol.deleteDuplicates(a)

while b:
    print(b.val)
    b = b.next