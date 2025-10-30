class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        n = len(s)
        i = 0
        while i < n and s[i] == " ":
            i += 1
        
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            sign = -1 if s[i] == "-" else 1
            i += 1
        
        num = 0
        while i < n and s[i].isdigit():
            d = ord(s[i]) - ord('0')
            num = num * 10 + d
            i += 1
        
        num *= sign
        INT_MAX, INT_MIN = 2**31-1, -2**31
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num

            
                
            