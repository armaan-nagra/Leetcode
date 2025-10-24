class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #manipulate string to get an arr of form ["i", 12, "iz", 4, "n"]
        tokens = []
        j = 0 
        m = len(abbr)
        while j < m:
            if abbr[j].isalpha():
                start = j 
                while j < m and abbr[j].isalpha():
                    j += 1
                tokens.append(abbr[start:j])
            else:
                start = j
                while j < m and abbr[j].isdigit():
                    j += 1
                num_str = abbr[start:j]
                if num_str[0] == "0":
                    return False
                tokens.append(int(num_str))

        i, n = 0, len(word)
        for tok in tokens:
            if isinstance(tok, int):
                i += tok
                if i > n:
                    return False 
            else:
                k = len(tok)
                if i + k > n or word[i:i+k] != tok:
                    return False 
                i += k 
        
        return i == n





        