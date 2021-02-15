class Solution:
    def numTrees(self, n: int) -> int:
        arr = [1, 1]

        if n == 1:
            return 1
        for k in range(2, n + 1):
            tmp = 0
            for i in range(k):
                l = i
                r = k - 1 - i
                tmp += arr[l] * arr[r]
            arr.append(tmp)

        return arr[n]


if __name__ == "__main__":
    n = int(input())
    res = Solution().numTrees(n)
    print(res)
