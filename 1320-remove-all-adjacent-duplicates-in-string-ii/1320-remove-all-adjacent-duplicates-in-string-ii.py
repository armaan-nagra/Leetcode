class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #store (char, freq)
        for ch in s:
            if stack:
                if stack[-1][0] == ch:
                    freq = stack[-1][1]
                    stack.pop()
                    stack.append((ch, freq + 1))
                    if stack[-1][1] == k:     
                        stack.pop()
                else:
                    stack.append((ch, 1))
            else:
                stack.append((ch, 1))
        res = ""

        for ch, freq in stack:
            res += ch * int(freq)
        
        return res


