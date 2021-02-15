class Solution:
    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:

        h = {}
        harr = []
        for candidate in candidates:
            if candidate in h:
                h[candidate] += 1
            else:
                h[candidate] = 1

        for i in h:
            harr.append([i, h[i]])
        res = []
        comb = []

        def combinationSum2Helper(curr, val):

            if val > target:
                return
            elif val == target:
                res.append(comb.copy())

            for i in range(curr, len(harr)):
                karr = harr[i]
                candidate = karr[0]
                freq = karr[1]

                if freq == 0:
                    continue
                val += candidate
                harr[i][1] -= 1
                comb.append(candidate)
                combinationSum2Helper(i, val)
                comb.pop()
                val -= candidate
                harr[i][1] += 1

        combinationSum2Helper(0, 0)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        comb = []

        def combinationSum2Helper(curr, val):

            if val > target:
                return
            elif val == target:
                res.append(comb.copy())

            for i in range(curr, len(candidates)):
                candidate = candidates[i]

                if i > curr and candidates[i] == candidates[i - 1]:
                    continue

                val += candidate

                comb.append(candidate)
                combinationSum2Helper(i + 1, val)
                comb.pop()
                val -= candidate

        combinationSum2Helper(0, 0)
        return res
