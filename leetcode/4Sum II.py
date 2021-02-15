class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        h = {}
        for i in A:
            for j in B:
                t = i + j
                if t in h:
                    h[t] += 1
                else:
                    h[t] = 1

        count = 0
        for i in C:
            for j in D:
                t = -1 * (i + j)
                if t in h:
                    count += h[t]
        return count
