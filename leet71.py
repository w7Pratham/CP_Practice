class Solution:
    def simplifyPath(self, path):
        stack = []
        for node in path.split('/'):
            if node in ("","."):
                pass
            elif node == "..":
                if stack: stack.pop()
            else:
                stack.append(node)
        return "/" + "/".join(stack)
