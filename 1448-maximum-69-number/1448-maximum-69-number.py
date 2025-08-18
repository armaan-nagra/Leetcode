class Solution:
    def maximum69Number (self, num: int) -> int:
        stringNum = str(num)
        done = False
        res = ""
        for c in stringNum:
            if c == '6' and done == False:
                res += "9"
                done = True
            else:
                res+= c
        return int(res)

        