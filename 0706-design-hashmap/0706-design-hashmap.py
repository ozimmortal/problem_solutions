class MyHashMap:

    def __init__(self):
        self.keystore = []
        self.valuestore = []
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keystore:
            self.keystore.append(key)
            self.valuestore.append(value)
        else:
            idx = self.keystore.index(key)
            self.valuestore[idx] = value
        
    def get(self, key: int) -> int:
        if key in self.keystore:
            return self.valuestore[self.keystore.index(key)]
        return -1

    def remove(self, key: int) -> None:
        if key in self.keystore:
            idx = self.keystore.index(key)
            self.keystore[idx] = ""
            self.valuestore[idx] = ""
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)