class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            while stack and stack[-1] > 0 and x < 0:
                if abs(stack[-1]) < abs(x):
                    stack.pop()
                elif abs(stack[-1]) > abs(x):
                    x = 0
                else:
                    x = 0 
                    stack.pop()
            if x:
                stack.append(x)
        return stack