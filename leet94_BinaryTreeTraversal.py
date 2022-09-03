#https://assets.leetcode.com/users/andvary/image_1556551007.png

class Solution:
    def preOrder(self, root):
        return [root.val] + self.preOrder(root.left) + self.preOrder(root.right) if root else []

    def inOrder(self, root):
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right) if root else []

    def postOrder(self, root):
        return self.postOrder(root.left) + self.postOrder(root.right) + [root.val] if root else []
