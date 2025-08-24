import random
class RandomizedSet:

    def __init__(self):
        self.length = 0
        self.list = []
        self.pos = {}
        

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False 
        self.pos[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        valIndex = self.pos[val]
        lastItem = self.list[-1]
        self.list[valIndex] = lastItem
        self.pos[lastItem] = valIndex
        self.pos.pop(val)

        self.list.pop()
        return True


    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
