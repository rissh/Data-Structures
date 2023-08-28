
class UndergroundSystem:
    def __init__(self):
        self.customer_trip = {}
        
        
        self.trips = {}

    def checkIn(self, id, stationName, t):
        self.customer_trip[id] = [stationName, t]
        

    def checkOut(self, id, stationName, t):
        start_station, start_t = self.customer_trip.pop(id)
        trip = (start_station, stationName)
        travel_time = t - start_t
        
        if trip not in self.trips:
            self.trips[trip] = [travel_time, 1]
        else:
            total_t, times = self.trips[trip]
            self.trips[trip] = [total_t + travel_time, times + 1.0]
        

    def getAverageTime(self, startStation, endStation):
        return self.trips[(startStation, endStation)][0] / self.trips[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
