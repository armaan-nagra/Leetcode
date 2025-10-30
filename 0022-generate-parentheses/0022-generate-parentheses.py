class Solution(object):
    def generateParenthesis(self, n):  
        res = []

        def backtrack(openB, closeB, combination):
            if openB == closeB == n:
                res.append(combination)
            
            if openB < n:
                backtrack(openB + 1, closeB, combination + "(")
            
            if closeB < openB:
                backtrack(openB, closeB + 1, combination + ")")
        
        backtrack(0,0,"")
        return res
        
