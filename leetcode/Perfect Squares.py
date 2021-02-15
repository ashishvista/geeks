from collections import deque


class Solution:
    ans = {}

    def numSquares(self, n: int) -> int:
        if n in self.ans:
            return self.ans[n]
        q = deque()
        nums = []
        visited = set()
        i = 1
        while True:
            j = i * i
            if j > n:
                break
            elif j == n:
                return 1
            else:
                q.append(j)
                nums.append(j)
                visited.add(j)
                self.ans[j] = 1
            i += 1
            c = 1

        while q:
            ln = len(q)
            while ln > 0:
                item = q.popleft()
                for num in nums:
                    nitem = item + num
                    if nitem == n:
                        return c + 1
                    elif nitem < n and nitem not in visited:
                        q.append(nitem)
                        visited.add(nitem)
                        self.ans[nitem] = c + 1
                ln -= 1
            c += 1
        return -1


if __name__ == "__main__":
    n = int(input())
    res = Solution().numSquares(n)
    print(res)
