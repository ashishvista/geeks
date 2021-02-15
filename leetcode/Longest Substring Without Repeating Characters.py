class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        start = 0
        hash = {}
        l = 0

        for i, v in enumerate(s):
            if v in hash and hash[v] >= start:
                start = hash[v] + 1

                if l > longest:
                    longest = l

                l = i - hash[v]

                hash[v] = i

            else:
                hash[v] = i
                l += 1

        if l > longest:
            longest = l

        return longest


if __name__ == "__main__":
    s = input()
    ss = Solution()
    res = ss.lengthOfLongestSubstring(s)
    print(res)
