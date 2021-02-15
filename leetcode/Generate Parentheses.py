from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opening = n
        strr = ""
        list = []
        arr = [[] for i in range(n + 1)]
        arr[0] = [""]
        for i in range(1, n + 1):
            for j in range(i):
                t1 = j
                t2 = i - 1 - j
                for p in arr[t1]:
                    for q in arr[t2]:
                        arr[i].append("(" + p + ")" + q)
        return arr[n]


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    list = s.generateParenthesis(n)
    print(list)
