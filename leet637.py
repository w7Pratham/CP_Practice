# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        result = []
        level = (root,)
        while level:
            result.append(sum(node.val for node in level)/len(level))
            level = tuple(leaf for node in level for leaf in (node.left, node.right) if leaf)

        return result

a = Solution()
print(a.averageOfLevels([3,9,20,None,None,15,7]))
