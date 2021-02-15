from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # s = "##########################"

        s = ["#" for i in range(26)]
        hash = {}
        for v in strs:
            h = {}
            for ch in v:
                if ch in h:
                    h[ch] += 1
                else:
                    h[ch] = 1
            ss = list.copy(s)
            for k in h:
                o = ord(k) - 97
                ss[o] = str(h[k]) + "#"
            ss = "".join(ss)
            if ss in hash:
                hash[ss].append(v)
            else:
                hash[ss] = [v]

        res = []
        for k in hash:
            res.append(hash[k])
        return res


if __name__ == "__main__":
    strs = list(input().strip().split(" "))
    s = Solution().groupAnagrams(strs)
