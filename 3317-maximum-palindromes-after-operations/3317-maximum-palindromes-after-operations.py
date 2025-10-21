class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        freq = defaultdict(int)
        lengths = []
        for word in words:
            lengths.append(len(word))
            for ch in word:
                freq[ch] += 1
        pairs = sum(v//2 for v in freq.values())
        singles = sum(v % 2 for v in freq.values())

        lengths.sort()
        res = 0

        for L in lengths:
            need = L // 2
            if L % 2 == 0:
                if pairs >= need:
                    pairs -= need
                    res += 1
            else:
                if pairs >= need and (singles > 0 or pairs - need >= 1):
                    pairs -= need
                    if singles > 0:
                        singles -= 1
                    else:
                        pairs -= 1
                        singles += 1
                    res += 1


        return res
        
