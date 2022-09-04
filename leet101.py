class Solution:
    def isSymmetric(self, root):
        def sym(l,r):
            if not l and not r: return True
            if l and r and l.val == r.val:
                return sym(l.left, r.right) and sym(l.right, r.left)
            return False
        return sym(root, root)
