from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0]))
        oi = []
        oi.append(intervals[0])
        n = len(intervals)
        for i in range(1, n):
            curinterval = intervals[i]
            prev = oi.pop()
            print(prev)

            if curinterval[0] > prev[1]:
                oi.append(prev)
                oi.append(curinterval)
            else:
                lg = max(curinterval[1], prev[1])
                tmp = [prev[0], lg]
                oi.append(tmp)
        return oi
