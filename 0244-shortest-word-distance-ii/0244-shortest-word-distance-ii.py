class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.stringArr = wordsDict
        self.indices = defaultdict(list)
        for index, value in enumerate(self.stringArr):
            self.indices[value].append(index)
        print(self.indices)

    def shortest(self, word1: str, word2: str) -> int:
        first = self.indices[word1]
        second = self.indices[word2]
        best = float('inf')
        l = r = 0

        while l<len(first) and r <len(second):
            best = min(best, abs(second[r] - first[l]))

            if first[l] < second[r]:
                l += 1
            else:
                r+=1
        return best






# # Your WordDistance object will be instantiated and called as such:
# # obj = WordDistance(wordsDict)
# # param_1 = obj.shortest(word1,word2)