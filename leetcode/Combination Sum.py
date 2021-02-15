class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        self.combinationSumHelper(candidates, target, res, [], n, 0)
        return res

    def combinationSumHelper(self, candidates, target, res, uc, n, i):

        for k in range(i, n):
            v = candidates[k]
            uc.append(v)
            vv = target - v

            if vv < 0:
                uc.pop()
                return

            if vv == 0:
                res.append(list.copy(uc))
                uc.pop()
                return

            self.combinationSumHelper(candidates, vv, res, uc, n, k)
            uc.pop()
