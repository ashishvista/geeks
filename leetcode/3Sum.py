from typing import List


class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        print()
        n = len(nums)
        list = []
        dups = {}
        for i in range(0, n - 2):
            j = i + 1
            s = nums[i] * -1
            self.find2sum(j, nums, s, list, i, n, dups)
        return list

    def find2sum(self, start, nums, s, list, i, n, dups):
        hash = {}
        for j in range(start, n):
            v = nums[j]
            r = s - v
            if r in hash:
                arr = [nums[i], v, r]
                # list.append(arr)
                if arr[0] > arr[1]:
                    arr[0], arr[1] = arr[1], arr[0]
                if arr[0] > arr[2]:
                    arr[0], arr[2] = arr[2], arr[0]
                if arr[1] > arr[2]:
                    arr[1], arr[2] = arr[2], arr[1]

                ss = str(arr[0]) + str(arr[1]) + str(arr[2])
                if ss not in dups:
                    dups[ss] = 1
                    list.append(arr)
            else:
                hash[v] = 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print()
        n = len(nums)
        list = []
        dups = {}
        nums.sort()
        for i in range(0, n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            s = nums[i] * -1
            self.find2pointer(j, nums, s, list, i, n, dups)
        return list

    def find2pointer(self, start, nums, s, list, i, n, dups):
        st = start
        et = n - 1
        dupss = {}
        if nums[i] == 0:
            if nums[start] == 0 and nums[start + 1] == 0:
                list.append([0, 0, 0])
            return

        elif nums[start] > s or nums[n - 1] + nums[n - 2] < s:
            return

        while st < et:
            p = nums[st] + nums[et]
            if p == s:
                list.append([nums[i], nums[st], nums[et]])
                while st < et and nums[st] == nums[st + 1]:
                    st += 1
                    continue
                while et > st and nums[et] == nums[et - 1]:
                    et -= 1
                    continue
                # ss = str(nums[st]) + str(nums[et])
                #
                # if ss not in dupss:
                #     dupss[ss] = 1
                #     list.append([nums[i], nums[st], nums[et]])

                st += 1
                et -= 1
            elif p < s:
                st += 1
            else:
                et -= 1


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(',')))
    s = Solution()
    l = s.threeSum(arr)
    print(l)
