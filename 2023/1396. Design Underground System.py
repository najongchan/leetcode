# https://leetcode.com/problems/design-underground-system/
class UndergroundSystem:

    def __init__(self):
        self.check = dict()
        self.trip = list()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check:
            self.trip.append((self.check[id][0], stationName, t - self.check[id][1]))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        logs = []
        for depart, arrive, t in self.trip:
            if depart == startStation and arrive == endStation:
                logs.append(t)

        return sum(logs) / len(logs)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
