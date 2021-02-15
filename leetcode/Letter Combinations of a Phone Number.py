from typing import List


class Solution:
    res = []
    hash = {

        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",

    }

    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        self.letterCombinationsHelper(digits, 0, "")
        return self.res

    def letterCombinationsHelper(self, digits, i, ss):
        if i == len(digits):
            if ss != "":
                self.res.append(ss)
            return

        v = self.hash[digits[i]]
        for j in v:
            self.letterCombinationsHelper(digits, i + 1, ss + j)


if __name__ == "__main__":
    digits = input().strip()[1:-1]
    s = Solution().letterCombinations(digits)
    print(s)
