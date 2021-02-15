from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        h = set(nums)
        long = 1
        for cv in h:
            if cv - 1 in h:
                continue

            l = 1
            cv = cv + 1
            while cv in h:
                l += 1
                cv += 1

            long = max(long, l)

        return long


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    s = Solution().longestConsecutive(arr)
    print(s)
