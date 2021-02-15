class Solution:
    def isValid(self, s: str) -> bool:
        print()
        st = []
        n = len(s)
        st.append(s[0])
        hash = {")": "(", "}": "{", "]": "["}
        # hash = {"(": ")", "{": "}", "[": "]"}

        for i in range(1, n):
            if st:
                top = st[-1]
            else:
                st.append(s[i])
                continue

            if s[i] not in hash:
                st.append(s[i])
            elif s[i] in hash and hash[s[i]] == top:
                st.pop()
            else:
                return False

        if st:
            return False
        else:
            return True


if __name__ == "__main__":
    s = input()[1:-1]
    ss = Solution()
    res = ss.isValid(s)
    print(res)
