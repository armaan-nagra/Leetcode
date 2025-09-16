class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""

        newPath = [p for p in path.split('/') if p]

        for x in newPath:
            if x == ".." and stack:
                stack.pop()
            elif x == ".":
                continue
            elif x != ".." and x != ".":
                stack.append(x)
        
        for y in stack:
            res+="/"+y
        if not stack:
            return "/"
        
        return res