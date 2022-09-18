# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        cac = []
        def traversal(start,ls,i):
            if not start.left or not start.right:
                return None
            if not i%2:
                ls.extend([start.left.val,start.right.val])
            traversal(start.left,ls,i+1)
            traversal(start.right,ls,i+1)
            return start
        traversal(root,cac,0)
        
        def switch(start,ls1, i):
            if not start.left or not start.right:
                return None
            if not i%2:
                start.right.val, start.left.val = ls1.pop(0), ls1.pop(0)
            switch(start.right,ls1,i+1)
            switch(start.left,ls1,i+1)
            return start
        switch(root,cac,0)
        
        return root
