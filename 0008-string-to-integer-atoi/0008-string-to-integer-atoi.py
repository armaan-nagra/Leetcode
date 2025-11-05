class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0

        while i < n and s[i] == " ":
            i += 1
        
        sign = 1
        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            else:
                sign = 1
            i += 1
        
        num = 0
        while i < n and s[i].isdigit():
            #miss out any leading zeros
            if num == 0 and s[i] == "0":
                i += 1
                continue
            value = ord(s[i]) - ord('0')
            num = num * 10 + value
            i += 1

        if num * sign > 2**31 - 1:
            return 2**31-1
        if num * sign < -2**31:
            return -2**31

        return sign * num
        





            
                
            