from typing import List


class Solution:
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
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    print(s.largestRectangleArea(arr))
