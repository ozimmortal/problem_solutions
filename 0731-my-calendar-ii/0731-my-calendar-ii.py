class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaping = []

    def book(self, startTime: int, endTime: int) -> bool:
        count = 0

        # check if it overlaps 
        for s , e in self.overlaping:
            if not (endTime <= s or e <= startTime):
                return False

        # add the event
       
        for s , e in self.events:
            if not (endTime <= s or e <= startTime):
                self.overlaping.append([max(s , startTime) , min(e , endTime)])
                
       
        self.events.append([startTime , endTime])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)