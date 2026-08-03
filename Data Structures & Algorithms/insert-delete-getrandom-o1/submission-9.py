import random
class RandomizedSet:

    def __init__(self):
        self.array = []
        self.seen = {}

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        else:
            self.seen[val] = len(self.array)
            self.array.append(val)
            return True 

    def remove(self, val: int) -> bool:
        if val not in self.seen:
            return False
        else:

            remove_index = self.seen[val]
            last_value = self.array[-1]

            self.seen[last_value] = remove_index
            self.array[remove_index] = last_value

            
            
            self.array.pop()
            del self.seen[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()