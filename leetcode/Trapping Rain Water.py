from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        maxLeft = [0 for i in range(n)]
        maxRight = [0 for i in range(n)]

        maxx = height[0]
        for i in range(n):
            if height[i] > maxx:
                maxx = height[i]
            maxLeft[i] = maxx

        maxx = height[n - 1]
        for i in range(n - 1, -1, -1):
            if height[i] > maxx:
                maxx = height[i]
            maxRight[i] = maxx

        sum = 0
        for i in range(n):
            p = min(maxLeft[i], maxRight[i])
            p = p - height[i]
            p = max(p, 0)
            sum += p
        return sum

    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        maxLeft = height[0]
        maxRight = height[n - 1]
        sum = 0
        i = 0
        j = n - 1

        while i <= j:
            if maxLeft < maxRight:
                sum += maxLeft - height[i]
                i += 1
                maxLeft = max(maxLeft, height[i])
            else:
                sum += maxRight - height[j]
                j -= 1
                maxRight = max(maxRight, height[j])

        return sum

    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        sum = 0
        i = 0
        st = [0]

        for i in range(1, n):
            while True:
                top = height[st[-1]]
                if height[i] < top:
                    st.append(i)
                    break
                elif height[i] == top:
                    st.pop()
                    st.append(i)
                    break
                else:
                    top = height[st.pop()]
                    if len(st) == 0:
                        st.append(i)
                        break
                    else:
                        minn = min(height[st[-1]], height[i])
                        distance = i - st[-1] - 1
                        diff = minn - top
                        sum += diff * distance

        return sum


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    res = s.trap(arr)
    print(res)
