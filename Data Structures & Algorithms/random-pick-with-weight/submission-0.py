import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        indices = list(range(len(self.w)))
        return random.choices(indices, weights=self.w, k=1)[0]