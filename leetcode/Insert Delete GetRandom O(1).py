from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.h:
            return False
        else:
            self.arr.append(val)
            self.h[val] = len(self.arr) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.h:
            cur_index = self.h[val]
            lst_elem = self.arr[len(self.arr) - 1]
            self.h[lst_elem] = cur_index
            self.arr[cur_index] = lst_elem
            del self.h[val]
            self.arr.pop()

            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.arr[randint(0, len(self.arr)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
