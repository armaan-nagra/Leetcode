class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)

        for x in arr:
            freq[x] += 1
        
        freq_freq = defaultdict(int)

        for char, fr in freq.items():
            freq_freq[fr] += 1
        
        for x, y in freq_freq.items():
            if y > 1:
                return False
        
        return True

        
