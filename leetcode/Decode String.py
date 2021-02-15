class Solution:
    def decodeString(self, s: str) -> str:
        curi = 0
        n = len(s)
        st = []
        while curi < n:
            if s[curi] == "[":
                st.append(curi)
                curi += 1
            elif s[curi] == "]":
                top = st.pop()
                ks = self.getK(s, top)

                k = int(ks)
                ps = self.decodeStringHelper(s, top, curi, k)
                s = s[0:top - len(ks)] + ps + s[curi + 1:]
                curi = top - len(ks) + len(ps)
                n=len(s)
            else:
                curi += 1
        return s

    def decodeStringHelper(self, s, i, j, k):
        ss = s[i + 1:j]
        ps = ""
        for j in range(k):
            ps += ss
        return ps

    def getK(self, s, i):
        i = i - 1
        ks = ""
        while s[i].isdigit():
            ks += s[i]
            i -= 1
        ks = ks[::-1]
        return ks


if __name__ == "__main__":
    s = input()
    res = Solution().decodeString(s)
    print(res)
