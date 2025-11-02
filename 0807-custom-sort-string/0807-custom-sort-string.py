class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #have a hash map with char -> index for order

        # orderMap = defaultdict(int)

        # for i, x in enumerate(order):
        #     orderMap[x] = i
         
        freq = Counter(s) #character in s -> frequency

        res = []

        for char in order:
            if char in freq:
                res += [char] * freq[char]
                del freq[char]
        

        for ch, fr in freq.items():
            res += [ch] * fr
        
        return "".join(res)


        
