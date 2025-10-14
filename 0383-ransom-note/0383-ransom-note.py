class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for x in ransomNote:
            if ransomCounter[x] > magazineCounter[x]:
                return False
        
        return True