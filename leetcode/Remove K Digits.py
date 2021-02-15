from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= len(num):
            return "0"
        if n == 1 or k == 0:
            return num
        dq = deque([0])
        ss = ""

        for i in range(1, n):
            curr = int(num[i])

            while True:
                if dq and curr < int(num[dq[-1]]):
                    dq.pop()
                else:
                    break
            dq.append(i)
            if i >= k:
                ss = ss + num[dq[0]]
                dq.popleft()

        return str(int(ss))


if __name__ == "__main__":
    num = input().strip()[1:-1]
    k = int(input().strip())
    res = Solution().removeKdigits(num, k)
    print(res)
