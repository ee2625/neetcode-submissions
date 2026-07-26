import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        self.arr.append(val)
        self.index[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        remove_index = self.index[val]
        last_value = self.arr[-1]

        self.arr[remove_index] = last_value
        self.index[last_value] = remove_index
        self.arr.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()