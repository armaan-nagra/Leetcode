class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []

        for index, char in enumerate(s):
            if char == "(":
                leftStack.append(index)
            elif char == "*":
                starStack.append(index)
            
            else: # char == ")"
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False

        while leftStack and starStack:
            if leftStack[-1] < starStack[-1]:
                leftStack.pop()
                starStack.pop()
            else:
                return False 
        return not leftStack



            

        
        