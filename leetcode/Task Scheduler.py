from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash = {}
        for v in tasks:
            if v in hash:
                hash[v] += 1
            else:
                hash[v] = 1
        del tasks
        arr = []
        for v in hash:
            arr.append(hash[v])
        del hash

        arr.sort()
        n = n + 1
        pn = len(arr)
        total = 0
        while True:
            t = 0
            for i in range(pn - 1, -1, -1):
                if arr[i] == 0:
                    break
                else:
                    arr[i] -= 1
                t += 1

                if t == n:
                    break

            total = total + n

            arr.sort()
            if arr[-1] == 0:
                total = total - n + t
                break

        return total


if __name__ == "__main__":
    arr = input().strip()[1:-1].split(",")
    n = int(input())
    res = Solution().leastInterval(arr, n)
    print(res)
