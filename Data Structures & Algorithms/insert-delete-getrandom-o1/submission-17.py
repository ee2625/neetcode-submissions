import random
class RandomizedSet:

    def __init__(self):
        self.array = []
        self.seen = {}

    def insert(self, val: int) -> bool:
        if val not in self.seen:
            self.seen[val] = len(self.array)
            self.array.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.seen:

            last_number = self.array[-1]
            remove_index = self.seen[val]

            self.seen[last_number] = remove_index
            self.array[remove_index] = last_number

            self.array.pop()
            del self.seen[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.array)
        
