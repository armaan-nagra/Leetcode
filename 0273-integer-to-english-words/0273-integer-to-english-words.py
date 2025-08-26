class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
        }
        if num == 0:
            return d[0]

        #convert any number less than 1000 into words
        def convert_helper(n): 
            if n == 0:
                return ""
            parts = []
            if n >= 100:
                parts.append(d[n//100] + " Hundred")
                n = n % 100
            if n >= 20:
                parts.append(d[(n//10) * 10])
                n = n % 10
            if n > 0 and n < 20:
                parts.append(d[n])
            return " ".join(parts)
        
        words = []
        i = 0
        scales = ["", "Thousand", "Million", "Billion"]

        while num > 0:
            chunk = num % 1000
            if chunk:
                chunk_words = convert_helper(chunk)
                words.append(chunk_words + " " + scales[i])
            num = num // 1000
            i += 1
        
        return " ".join(reversed(words)).strip()


        



