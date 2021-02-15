from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ss = []
        n = len(T)
        res = [0] * n
        for i in range(n):
            while ss and T[i] > T[ss[-1]]:
                t = ss.pop()
                res[t] = i - t
            ss.append(i)

        return res


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    s = Solution()
    res = s.dailyTemperatures(arr)
    print(res)
