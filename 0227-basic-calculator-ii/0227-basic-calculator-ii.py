class Solution(object):
    def calculate(self, s):
        res = 0
        last = 0
        cur = 0
        op = '+'
        n = len(s)

        for i, ch in enumerate(s):
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            
            if ch in "+-/*" or i == n - 1:
                if op == "+":
                    res += last
                    last = cur
                elif op == "-":
                    res += last 
                    last = -cur
                elif op == "*":
                    last = last * cur
                else:
                    last = int(float(last) / cur)
                op = ch
                cur = 0
        return res + last




















        # stack = []
        # #split string into values and operators
        # tokens = re.findall(r'\d+|[+\-*/]', s)
        
        # #first loop, if you see a * or /, then do it
        # counter = 0
        # n = len(tokens)
        # while counter < n:
        #     x = tokens[counter]
        #     if x == "*" or x == "/":
        #         value1 = stack.pop()
        #         value2 = int(tokens[counter+1])
        #         if x == "*":
        #             stack.append(value1 * value2)
        #         if x == "/":
        #             stack.append(value1 // value2)
        #         counter += 2    
        #     else:
        #         if str(x).isdigit():
        #             stack.append(int(x))
        #         else:
        #             stack.append(x)
        #         counter += 1

        # res = stack[0]
        # i = 1
        # while i < len(stack):
        #     op = stack[i]
        #     num = stack[i+1]
        #     if op == "+":
        #         res += num
        #     else:
        #         res -= num 
        #     i += 2
        # return res
                
        
            




        