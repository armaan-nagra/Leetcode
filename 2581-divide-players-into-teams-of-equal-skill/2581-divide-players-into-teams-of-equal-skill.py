class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #sort items and then use left and right pointers to add together
        n = len(skill)
        if n % 2 != 0:
            return -1
        l, r = 0, n -1
        skill.sort()

        groups = 0
        count = None
        while l < r:
            if not count:
                count = skill[l] + skill[r]
                groups = groups + (skill[l] * skill[r])
            else:
                curr = skill[l] + skill[r]
                if curr != count:
                    return -1 
                groups = groups + (skill[l] * skill[r])

            l += 1
            r -= 1
        return groups
