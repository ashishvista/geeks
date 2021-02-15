from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        start = 0
        n = len(nums)
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if start != end and nums[start] > nums[end]:
                if nums[mid] >= nums[start] and target <= nums[end]:
                    start = mid + 1
                elif nums[mid] < nums[start] and target > nums[end]:
                    end = mid - 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        n = len(nums)
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    tar = int(input())
    res = Solution().search(arr, tar)
    print(res)
