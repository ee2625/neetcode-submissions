import random
class RandomizedSet:

    def __init__(self):
        self.ans = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val not in self.index:
            self.index[val] = len(self.ans)
            self.ans.append(val)
            
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index:
            self.ans.remove(val)
            del self.index[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.ans[random.randint(0,len(self.ans)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()