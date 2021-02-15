from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]

        if num == 0:
            return res
        i = 0

        while True:
            ln = len(res)
            j = 0
            while j < ln:
                res.append(1 + res[j])
                j += 1
                i += 1
                if i == num:
                    return res


if __name__ == "__main__":
    num = int(input())
    res = Solution().countBits(num)
    print(res)
