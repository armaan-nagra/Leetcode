class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openBrackets = 0
        res = []

        for char in s: #first loop to only have as many closed <= open
            if char == "(":
                res.append(char)
                openBrackets += 1
            elif char == ")":
                if openBrackets:
                    res.append(char)
                    openBrackets -= 1
            else:
                res.append(char) 
        
        #second loop to make sure there's no unclosed brackets, if so, remove them
        counter = len(res) - 1
        while openBrackets and counter >= 0:
            if res[counter] == "(":
                openBrackets -= 1
                res.pop(counter)
            counter -= 1

        return "".join(res)

            
        

            






