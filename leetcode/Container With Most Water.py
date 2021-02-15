from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        n = len(height)

        i = 0
        j = n - 1
        if height[i] < height[j]:
            max = height[i] * (j - i)
        else:
            max = height[j] * (j - i)

        while True:
            if height[i] < height[j]:
                temp = i + 1
                while temp <= j and height[temp] < height[i]:
                    temp += 1
                i = temp
            else:
                temp = j - 1
                while temp >= i and height[temp] < height[j]:
                    temp -= 1
                j = temp

            if i >= j:
                return max
            elif height[i] < height[j]:
                area = height[i] * (j - i)
            else:
                area = height[j] * (j - i)

            if max < area:
                max = area

        return max


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    res = s.maxArea(arr)
    print(res)
