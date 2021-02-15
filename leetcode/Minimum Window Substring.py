class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h = {}
        self.num_req_chars = 0

        for ch in t:
            if ch in h:
                h[ch] += 1
            else:
                h[ch] = 1
            self.num_req_chars += 1

        start = 0
        end = -1
        for ch in s:
            self.updateSIncoming(ch, h)
            end += 1
            if self.num_req_chars == 0:
                break

        if self.num_req_chars != 0:
            return ""
        res = [start, end]
        k = s[start:end + 1]
        sn = len(s) - 1

        while end <= sn:
            if start != 0:
                sch = s[start - 1]
                ech = s[end]
                self.updateSIncoming(ech, h)
                self.updateSOutgoing(sch, h)
            if self.num_req_chars == 0:
                while start < end:
                    tch = s[start]
                    if self.checkifchcanberemoved(tch, h):
                        self.updateSOutgoing(tch, h)
                        start += 1
                    else:
                        break
            if (end - start) < (res[1] - res[0]):
                res = [start, end]

            start += 1
            end += 1

        return s[res[0]:res[1] + 1]

    def updateSIncoming(self, ch, h):
        if ch in h:
            if h[ch] > 0:
                self.num_req_chars -= 1
            h[ch] -= 1

    def updateSOutgoing(self, ch, h):
        if ch in h:
            if h[ch] >= 0:
                self.num_req_chars += 1
            h[ch] += 1

    def checkifchcanberemoved(self, ch, h):
        if ch not in h or (ch in h and h[ch] < 0):
            return True
        else:
            return False


if __name__ == "__main__":
    s = input()[1:-1]
    t = input()[1:-1]
    res = Solution().minWindow(s, t)
    print(res)
