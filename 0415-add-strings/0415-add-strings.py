class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        n = len(num1)
        m = len(num2)

        carry = 0

        m_counter = 0
        n_counter = 0

        while m_counter < m or n_counter < n:
            val_1 = 0
            val_2 = 0
            if n_counter < n:
                val_1 = ord(num1[n-n_counter-1]) - ord('0')
            if m_counter < m:
                val_2 = ord(num2[m-m_counter-1]) - ord('0')
            total = val_1 + val_2 + carry
            
            carry = total // 10
            slide_in = total % 10
            res.append(chr(ord('0') + slide_in))
            m_counter += 1
            n_counter += 1
        
        if carry:
            res.append(chr(ord('0') + carry))
        
        res.reverse()
        return "".join(res)
                
        

        