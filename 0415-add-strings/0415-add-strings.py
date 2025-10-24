class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        counter = 1
        n = len(num1)
        m = len(num2)
        carry = 0
        res = ""
        while counter <= n or counter <= m:
            m_total = 0
            n_total = 0
            if counter <= n:
                n_total += ord(num1[n - counter]) - 48
                if num1[n-counter] == "0":
                    n_total = 0

            if counter <= m:
                m_total += ord(num2[m - counter]) - 48
                if num2[m-counter] == "0":
                    m_total = 0
            
            total = carry + m_total + n_total
            print(total)
            counter += 1
            carry = total // 10
            value = total % 10
            res = res + str(value)
        if carry != 0:
            res = res + (str(carry))
        
        return res[::-1]

        