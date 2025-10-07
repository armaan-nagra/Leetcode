class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        if n < 4:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4

        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False 
        
        sides = [0] * 4

        def dfs(i: int) -> bool:
            if i == n:
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            stick = matchsticks[i]

            seen = set() #why is this used
            for k in range(4):
                if sides[k] + stick > target:
                    continue
                if sides[k] in seen:
                    continue
                
                seen.add(sides[k])
                sides[k] += stick
                if dfs(i+1):
                    return True
                sides[k] -= stick

                if sides[k] == 0:
                    break
            return False
        
        return dfs(0)
