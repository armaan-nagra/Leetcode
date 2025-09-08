class Solution:
    def minSteps(self, s: str, t: str) -> int:
        #use a hash map?
        charFreqS = [0] * 26
        charFreqT = [0] * 26
        res = 0

        for char in s:
            charFreqS[ord(char)-97] += 1

        for char in t:
            charFreqT[ord(char)-97] += 1
        
        for x in range(26):
            if charFreqS[x] < charFreqT[x]:
                res += charFreqT[x] - charFreqS[x]
            
        return res

        
        