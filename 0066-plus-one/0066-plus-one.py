class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        carry = 1

        while i >= 0:
            value = digits[i] + carry 
            if value <= 9:
                digits[i] = value
                return digits
            else:
                carry = value // 10
                digits[i] = value % 10
                i -= 1
        if carry:
            digits = [carry] + digits
        return digits


