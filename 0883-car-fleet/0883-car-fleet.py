class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        #sort positions in increasing order and also the speed relative to it
        for x in range(len(position)):
            cars.append((position[x], speed[x]))
        cars.sort()
        
        #loop through each position, check top position, and if you'll reach the end before it, pop and add new
         
        for distance, speed in cars:
            time = (target - distance) / speed
            while stack and ((target - stack[-1][0]) / stack[-1][1]) <= time:
                stack.pop()
            stack.append((distance,speed))


        return len(stack)