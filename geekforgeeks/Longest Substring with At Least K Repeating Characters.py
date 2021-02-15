class Node:
    def __init__(self, i, n):
        self.i = i
        self.n = n


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        return self.longestSubstringHelper(s, 0, len(s) - 1, k)

    def longestSubstringHelper(self, s, start, end, k):
        if start > end:
            return 0
        h = {}
        hh = set()
        for i in range(start, end + 1):
            c = s[i]
            if c in hh:
                continue
            if c in h:
                h[c].n += 1
            else:
                h[c] = Node(i, 1)
            if h[c].n >= k:
                del h[c]
                hh.add(c)

        for c in h:
            i = h[c].i
            j = i
            while j <= end:
                if s[j] not in h:
                    break
                j += 1
            p1 = self.longestSubstringHelper(s, start, i - 1, k)
            p2 = self.longestSubstringHelper(s, j, end, k)
            return max(p1, p2)

        return end - start + 1


if __name__ == "__main__":
    s = input()[1:-1]
    k = int(input())
    res = Solution().longestSubstring(s, k)
    print(res)
