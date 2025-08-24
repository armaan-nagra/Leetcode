class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False 
        
        charStack = []

        brackets = {")" : "(", "]" : "[", "}" : "{"}

        for x in range(len(s)):
            if s[x] == "(" or s[x] == "[" or s[x] == "{":
                charStack.append(s[x])
            else:
                if len(charStack) == 0:
                    return False
                value = charStack.pop()
                if value != brackets[s[x]]:
                    return False
        
        if len(charStack) != 0:
            return False

        return True
