from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        dp = [0 for i in range(cols)]
        area = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "0":
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + int(matrix[i][j])
            tmp = self.largestRectangleArea(dp)
            area = max(area, tmp)
        return area

    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        i = 0
        area = 0
        n = len(heights)
        while True:
            if not st and i >= n:
                break
            if st and i >= n:
                top = heights[st.pop()]
                if st:
                    start = st[-1]
                else:
                    start = -1
                stop = n
                dist = stop - start - 1
                area = max(area, dist * top)
            elif not st:
                st.append(i)
                i += 1
            elif heights[st[-1]] <= heights[i]:
                st.append(i)
                i += 1
            elif heights[st[-1]] > heights[i]:
                top = heights[st.pop()]
                if st:
                    start = st[-1]
                else:
                    start = -1
                dist = i - start - 1
                area = max(area, dist * top)
            else:
                print("some case missing")
        return area


if __name__ == "__main__":
    r = int(input())
    arr = []
    for i in range(r):
        temp = list(input().strip().split())
        arr.append(temp)
    s = Solution().maximalRectangle(arr)
    print(s)
