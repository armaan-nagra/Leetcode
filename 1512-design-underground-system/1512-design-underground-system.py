class UndergroundSystem:

    def __init__(self):
        self.at = defaultdict(list) # id -> ['start station', check in time]
        self.routesTime = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.at[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, checkInTime = self.at[id]
        del self.at[id]

        self.routesTime[(checkInStation, stationName)].append(t-checkInTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        values = self.routesTime[(startStation, endStation)]
        return sum(values) / len(values)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)