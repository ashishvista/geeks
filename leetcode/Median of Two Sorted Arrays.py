from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        median_length = (n1 + n2 + 1) // 2
        start = 0
        end = median_length
        curr = 0
        other_curr = 0

        while start <= end:
            curr = (start + end) // 2  # assume size of nums1 to be used in final median half
            other_curr = median_length - curr

            if curr > n1:
                end = n1
                continue
            elif other_curr > n2:
                start = median_length - n2
                continue

            if other_curr < n2 and n1 > 0 and curr > 0 and nums1[curr - 1] > nums2[other_curr]:
                end = curr - 1
                continue
            elif curr < n1 and n2 > 0 and other_curr > 0 and nums1[curr] < nums2[other_curr - 1]:
                start = curr + 1
                continue
            else:
                break

        if curr == 0:
            m = nums2[other_curr - 1]
        elif other_curr == 0:
            m = nums1[curr - 1]
        else:
            m = max(nums1[curr - 1], nums2[other_curr - 1])

        if (n1 + n2) % 2 == 0:
            if curr < n1 and other_curr < n2:
                t = min(nums1[curr], nums2[other_curr])
            elif curr < n1:
                t = nums1[curr]
            else:
                t = nums2[other_curr]
            m = (m + t) / 2
        return m


if __name__ == "__main__":
    t1 = input()[1:-1].strip()
    t2 = input()[1:-1].strip()
    nums1 = []
    nums2 = []
    if len(t1) > 0:
        nums1 = list(map(int, t1.split(",")))
    if len(t2) > 0:
        nums2 = list(map(int, t2.split(",")))
    t1 = t2 = None
    s = Solution()
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)
