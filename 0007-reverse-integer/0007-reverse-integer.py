class Solution:
    def reverse(self, x: int) -> int:
        value = str(x)
        new_value = ""
        if value[0] == '-':
            new_value+='-'
            value = value[1:]
         
        for x in range(len(value)-1,-1,-1):
            new_value+=value[x]
        
        new_value = int(new_value)

        if new_value > 2**31 - 1 or new_value < -2**31:
            return 0
        return int(new_value)
