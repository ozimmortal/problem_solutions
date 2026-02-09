class RandomizedSet:

    def __init__(self):
        self.e = {}
        self.d = []
    def insert(self, val: int) -> bool:
        if val not in self.e:
            self.e[val] = len(self.d)
            self.d.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.e:
            b_i = self.e[val]
            self.e[self.d[-1]] = b_i
            
            temp = self.d[b_i]
            self.d[b_i] = self.d[-1]
            self.d[-1] = temp

            del self.e[val]
            self.d.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        random_index  = random.randrange(0,len(self.d))
        if len(self.d) == 0:
            return []
        return self.d[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()