import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.seen = {}

    def insert(self, val: int) -> bool:
        if val not in self.seen:
            self.seen[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False
            

    def remove(self, val: int) -> bool:
        if val not in self.seen:
            return False
        else:

            last_item = self.arr[-1]
            remove_index = self.seen[val]

            self.arr[remove_index] = last_item
            self.seen[last_item] = remove_index

            self.arr.pop()
            del self.seen[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()