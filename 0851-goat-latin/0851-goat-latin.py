class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentenceList = sentence.split(" ")
        res = []
        for idx, word in enumerate(sentenceList):
            newWord = word
            if newWord[0].lower() in "aeiou":
                newWord += "ma"
            elif newWord[0].lower() in "bcdfghjklmnopqrstvwxyz":
                frontValue = newWord[0]
                newWord = newWord[1:]
                newWord += frontValue
                newWord += "ma"
            
            for y in range(idx+1):
                newWord += "a"
        
            res.append(newWord)

        return " ".join(res)
        
