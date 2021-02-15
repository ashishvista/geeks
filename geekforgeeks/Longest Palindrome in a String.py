def longestPalindrome(s):
    n = len(s)
    longestP = 1
    pIndex = [0, 0]
    for i in range(n):
        for j in range(i + 1, n):
            pSize = j - i + 1
            if pSize > longestP and isPalindrome(s, i, j):
                longestP = pSize
                pIndex[0] = i
                pIndex[1] = j
    for i in range(pIndex[0], pIndex[1] + 1):
        print(s[i], end="")


def isPalindrome(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low = low + 1
        high = high - 1
    return True


def longestPalindrome2(s):
    low = 0
    high = len(s) - 1
    p = [1, 0, 0]
    dp = [[-1 for i in range(len(s))] for i in range(len(s))]
    isPalindrome2(s, low, high, p, dp)
    for i in range(p[1], p[2] + 1):
        print(s[i], end="")


def isPalindrome2(s, low, high, p, dp):
    if dp[low][high] != -1:
        return dp[low][high]
    if low == high or low > high:
        return True

    psize = high - low + 1
    if s[low] == s[high] and isPalindrome2(s, low + 1, high - 1, p, dp):
        if psize > p[0]:
            p[0] = psize
            p[1] = low
            p[2] = high
        dp[low][high] = True
        return True

    if psize - 1 > p[0]:
        isPalindrome2(s, low, high - 1, p, dp)
        isPalindrome2(s, low + 1, high, p, dp)
    dp[low][high] = False
    return False


def longestPalindrome3(s):
    p = [1, 0, 0]
    n = len(s)
    dp = [[-1 for i in range(len(s))] for i in range(len(s))]
    for i in range(n):
        for j in range(n - i):
            low = j
            high = low + i
            l = high - low + 1

            if low == high:
                dp[low][high] = True
                continue
            if low + 1 == high:
                if s[low] == s[high]:
                    dp[low][high] = True
                    if p[0] < l:
                        p[0] = l
                        p[1] = low
                        p[2] = high
                else:
                    dp[low][high] = False
                continue

            if dp[low + 1][high - 1] and s[low] == s[high]:
                dp[low][high] = True
                if p[0] < l:
                    p[0] = l
                    p[1] = low
                    p[2] = high
            else:
                dp[low][high] = False

    for i in range(p[1], p[2] + 1):
        print(s[i], end="")


def longestPalindrome4(s):
    p = [1, 0, 0]
    n = len(s)

    # generate all odd palindromes
    for i in range(n):
        for j in range(1, n):
            low = i - j
            high = i + j
            l = high - low + 1
            if low < 0 or high > n - 1:
                break
            if s[low] == s[high]:
                if p[0] < l:
                    p[0] = l
                    p[1] = low
                    p[2] = high
            else:
                break
    # generate all even palindromes
    for i in range(n):
        for j in range(n):
            low = i - j
            high = i + 1 + j
            l = high - low + 1
            if low < 0 or high > n - 1:
                break
            if s[low] == s[high]:
                if p[0] < l:
                    p[0] = l
                    p[1] = low
                    p[2] = high
            else:
                break
    for i in range(p[1], p[2] + 1):
        print(s[i], end="")


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        s = input()
        longestPalindrome4(s)
        print()
