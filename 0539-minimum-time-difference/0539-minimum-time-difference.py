class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #convert to minutes in 24 hour format and then find min difference?
        minuteTimePoints = []

        for x in timePoints:
            hour, minute = x.split(':')
            minuteTimePoints.append((60 * int(hour)) + int(minute))
        
        minuteTimePoints.sort()
        #there's only really two options, either it's the last and the first or any two in the middle?
        res = float('inf')
        for x in range(1, len(minuteTimePoints)):
            if minuteTimePoints[x] - minuteTimePoints[x-1] < res:
                res = minuteTimePoints[x] - minuteTimePoints[x-1]

        print(minuteTimePoints)
        if (minuteTimePoints[0] - minuteTimePoints[-1]) + 1440 < res:
            res = (minuteTimePoints[0] - minuteTimePoints[-1]) + 1440
        
        return res


        
