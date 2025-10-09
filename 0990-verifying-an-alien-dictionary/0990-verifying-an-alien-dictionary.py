class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = defaultdict(int)
        for i,c in enumerate(order):
            alphabet[c] = i
        
        for i in range(1,len(words)):
            w1, w2 = words[i-1], words[i]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if alphabet[w2[j]] < alphabet[w1[j]]:
                        return False 
                    break 
            else:
                if len(w1) > len(w2):
                    return False 
                
        return True
