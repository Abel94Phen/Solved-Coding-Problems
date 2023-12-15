class UndergroundSystem:

    def __init__(self):
        self.passengers = {}
        self.station_times = {} ## for the routes

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.passengers[id][0], stationName) not in self.station_times:
            self.station_times[(self.passengers[id][0], stationName)] = [0,0]
        self.station_times[(self.passengers[id][0], stationName)][0] += t - self.passengers[id][1]
        self.station_times[(self.passengers[id][0], stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_times[(startStation, endStation)][0] / self.station_times[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)