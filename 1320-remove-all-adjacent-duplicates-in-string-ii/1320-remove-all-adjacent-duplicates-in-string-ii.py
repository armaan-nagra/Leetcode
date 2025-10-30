class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #store items of type (char, counter)

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        result = ""
        for char, counter in stack:
            result += char * counter
        
        return result
        
            

















        # stack = []

        # for x in s:
        #     #keep checking last k elements in stack?
        #     stack.append(x)
        #     if len(stack) >= k:
        #         value = stack[-1]
        #         remove = True
        #         for y in range(1,k+1):
        #             if stack[-y] != value:
        #                 remove = False
        #         if remove:
        #             stack = stack[0:-k]
        # return "".join(stack)
                    
