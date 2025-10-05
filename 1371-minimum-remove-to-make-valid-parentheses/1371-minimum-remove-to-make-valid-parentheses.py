class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openBracket = 0
        res = []
        for character in s:
            if character == "(":
                openBracket += 1
                res.append(character)
            elif character == ")":
                if openBracket > 0:
                    res.append(character)
                    openBracket -= 1
            else:
                res.append(character)

        

        #now do the exact the same thing but go right to left and remove openBracket open brackets?

        for x in range(len(res)-1, -1, -1):
            if openBracket > 0:
                if res[x] == "(":
                    res.pop(x)
                    openBracket -= 1
                    

        return "".join(res)


