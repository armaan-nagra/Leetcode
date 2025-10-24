class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i+=1
                j+=1
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            else:
                sublen = 0
                while j < len(abbr) and not abbr[j].isalpha():
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen
        return i == len(word) and j == len(abbr)

















        
        # tokens = []
        # j = 0 
        # m = len(abbr)
        # while j < m:
        #     if abbr[j].isalpha():
        #         start = j 
        #         while j < m and abbr[j].isalpha():
        #             j += 1
        #         tokens.append(abbr[start:j])
        #     else:
        #         start = j
        #         while j < m and abbr[j].isdigit():
        #             j += 1
        #         num_str = abbr[start:j]
        #         if num_str[0] == "0":
        #             return False
        #         tokens.append(int(num_str))

        # i, n = 0, len(word)
        # for tok in tokens:
        #     if isinstance(tok, int):
        #         i += tok
        #         if i > n:
        #             return False 
        #     else:
        #         k = len(tok)
        #         if i + k > n or word[i:i+k] != tok:
        #             return False 
        #         i += k 
        
        # return i == n





        