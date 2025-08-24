class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        shortest = float('inf')
        wordIdx = {}
        wordIdx[word1] = float('inf')
        wordIdx[word2] = float('-inf')
        
        for x in range(len(wordsDict)):
            if wordsDict[x] == word1 or wordsDict[x] == word2:
                wordIdx[wordsDict[x]] = x
            
            if abs(wordIdx[word1] - wordIdx[word2]) < shortest:
                shortest = abs(wordIdx[word1] - wordIdx[word2])
        
        return shortest
            
