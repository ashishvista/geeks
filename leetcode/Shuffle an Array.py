from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.dup = nums.copy()

    def reset(self) -> List[int]:
        return self.dup

    def shuffle(self) -> List[int]:
        arr = self.dup.copy()
        self.shuffleHelper(arr, 0, len(arr)-1)
        return arr

    def shuffleHelper(self, arr, start, end):
        if start > end:
            return
        num = randint(start, end)
        arr[start], arr[num] = arr[num], arr[start]
        self.shuffleHelper(arr, start + 1, end)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
