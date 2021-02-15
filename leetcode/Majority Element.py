from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        for v in nums:
            if c == 0:
                ele = v
                c = 1
            elif ele == v:
                c += 1
            else:
                c -= 1
        return ele


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    print(s.majorityElement(arr))
