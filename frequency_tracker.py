class FrequencyTracker:

    def __init__(self):
        self.tracker = {}
        self.frequency = [0]*200001
        

    def add(self, number: int) -> None:
        if number not in self.tracker:
            self.tracker[number] = 0
        if self.tracker[number] != 0:
            self.frequency[self.tracker[number]] -= 1 
        self.tracker[number] += 1
        self.frequency[self.tracker[number]] += 1  



    def deleteOne(self, number: int) -> None:
        if number in self.tracker:
            self.frequency[self.tracker[number]] -= 1 
            self.tracker[number] -= 1
                
            if self.tracker[number] == 0:
                del self.tracker[number]
            else:
                self.frequency[self.tracker[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)