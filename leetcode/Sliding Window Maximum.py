from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque([])
        for i in range(k):
            while True:
                if len(dq) == 0 or nums[dq[-1]] > nums[i]:
                    dq.append(i)
                    break
                else:
                    dq.pop()
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            while True:
                if len(dq) == 0 or nums[dq[-1]] > nums[i]:
                    dq.append(i)
                    break
                else:
                    dq.pop()
            if dq[0] < (i - k + 1):
                dq.popleft()
            res.append(nums[dq[0]])
        return res


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(',')))
    k = int(input())
    s = Solution()
    res = s.maxSlidingWindow(arr, k)
    print(res)
