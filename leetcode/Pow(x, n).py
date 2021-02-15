class Solution:
    def myPow1(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            return self.myPowHelper(x, x, 1, n)
        else:

            return 1 / self.myPowHelper(x, x, 1, -1 * n)

    def myPowHelper1(self, ox, x, t, n):
        if t == n:
            return x
        if 2 * t <= n:
            t = 2 * t
            x = x * x
            return self.myPowHelper(ox, x, t, n)
        else:
            return x * self.myPowHelper(ox, ox, 1, n - t)

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            return self.myPowHelper(x, n)
        else:
            return 1 / self.myPowHelper(x, - 1 * n)

    def myPowHelper(self, x, n):
        if n == 1:
            return x
        p = self.myPowHelper(x, n // 2)
        if n % 2 == 0:
            return p * p
        else:
            return x * p * p
