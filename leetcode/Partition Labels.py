from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(s)
        hash = {}
        for i in range(n):
            hash[s[i]] = i

        res = []
        start = 0
        end = -1
        i = 0
        while i < n:
            end = max(hash[s[i]], end)
            if i == end:
                res.append(end - start + 1)
                start = i + 1
            i += 1

        return res


if __name__ == "__main__":
    s = input().strip()[1:-1]
    s = Solution().partitionLabels(s)
    print(s)
