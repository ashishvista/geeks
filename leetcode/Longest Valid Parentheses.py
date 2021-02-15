class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        longest = 0
        st = [-1]

        for i, ss in enumerate(s):
            if ss is "(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    longest = max(longest, i - st[-1])
        return longest

    def longestValidParentheses1(self, s: str) -> int:
        longest = 0
        left = 0
        right = 0
        n = len(s)
        for i in range(n):
            ss = s[i]
            if ss is "(":
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, left * 2)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0
        for i in range(n - 1, -1, -1):
            ss = s[i]
            if ss is ")":
                right += 1
            else:
                left += 1

            if left == right:
                longest = max(longest, left * 2)
            elif left > right:
                left = 0
                right = 0

        return longest

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        valid_dp = [0 for i in range(n)]
        longest = 0
        for i, ss in enumerate(s):
            if ss == "(":
                valid_dp[i] = 0

            else:
                opening_bracket_loc = i - valid_dp[i - 1] - 1
                if opening_bracket_loc >= 0 and s[opening_bracket_loc] == "(":
                    valid_dp[i] += valid_dp[i - 1] + 2

                    index_just_before_opening_bracket_loc = i - valid_dp[i - 1] - 2
                    if index_just_before_opening_bracket_loc >= 0:
                        valid_dp[i] += valid_dp[index_just_before_opening_bracket_loc]

                longest = max(longest, valid_dp[i])

        return longest


if __name__ == "__main__":
    s = input()[1:-1]
    print(Solution().longestValidParentheses(s))
