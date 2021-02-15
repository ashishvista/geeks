from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        req_chars = {}
        curr_chars = {}
        sn = len(s)
        pn = len(p)
        res = []
        remaining_req_chars_count = 0

        if pn > sn:
            return res

        for v in p:
            if v in req_chars:
                req_chars[v] += 1
            else:
                req_chars[v] = 1

        for i in range(pn):
            if s[i] in req_chars:
                if s[i] in curr_chars:
                    curr_chars[s[i]] += 1
                else:
                    curr_chars[s[i]] = 1

        for v in req_chars:
            if v in curr_chars:
                diff = req_chars[v] - curr_chars[v]
                if diff > 0:
                    remaining_req_chars_count += diff
            else:
                remaining_req_chars_count += req_chars[v]

        i = 0
        if remaining_req_chars_count == 0:
            res.append(i)

        for j in range(pn, sn):
            if s[i] != s[j]:
                if s[i] in req_chars:
                    if req_chars[s[i]] - curr_chars[s[i]] >= 0:
                        remaining_req_chars_count += 1
                    curr_chars[s[i]] -= 1

                if s[j] in req_chars:
                    if s[j] not in curr_chars:
                        curr_chars[s[j]] = 1
                        remaining_req_chars_count -= 1
                    else:
                        if req_chars[s[j]] - curr_chars[s[j]] > 0:
                            remaining_req_chars_count -= 1
                        curr_chars[s[j]] += 1

            if remaining_req_chars_count == 0:
                res.append(i + 1)

            i += 1

        return res


if __name__ == "__main__":
    t1 = input().strip()[1:-1]
    t2 = input().strip()[1:-1]
    ss = Solution().findAnagrams(t1, t2)
    print(ss)
