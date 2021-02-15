class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        total = 0
        mxw = weights[0]
        for w in weights:
            total += w
            mxw = max(mxw, w)

        avg_per_day = total // D
        res = float("+inf")
        low = max(avg_per_day, mxw)
        high = total
        while low <= high:
            mid = (low + high) // 2

            if self.check(weights, D, mid) < 0:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1

        return res

    def check(self, weights, D, wpd):
        d = 1
        s = 0
        i = 0

        while i < len(weights):
            w = weights[i]
            s += w
            if s > wpd:
                s = 0
                d += 1
            else:
                i += 1

        if d <= D:
            return -1
        else:
            return 1
