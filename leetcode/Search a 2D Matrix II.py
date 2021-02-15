class Solution:
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        start = 0
        end = n - 1
        colE = 0
        while start <= end:
            mid = (start + end) // 2

            if target == matrix[0][mid]:
                return True

            elif target < matrix[0][mid]:
                end = mid - 1
                colE = end
            else:
                start = mid + 1
                colE = end

        start = 0
        end = m - 1
        rowE = 0
        while start <= end:
            mid = (start + end) // 2

            if target == matrix[mid][0]:
                return True

            elif target < matrix[mid][0]:
                end = mid - 1
                rowE = end
            else:
                start = mid + 1
                rowE = end

        start = 0
        end = colE
        colS = 0
        while start <= end:
            mid = (start + end) // 2

            if target == matrix[rowE][mid]:
                return True

            elif target < matrix[rowE][mid]:
                end = mid - 1
                colS = start
            else:
                start = mid + 1
                colS = start

        start = 0
        end = rowE
        rowS = 0
        while start <= end:
            mid = (start + end) // 2

            if target == matrix[mid][colE]:
                return True

            elif target < matrix[mid][colE]:
                end = mid - 1
                rowS = start
            else:
                start = mid + 1
                rowS = start

        for i in range(rowS, rowE + 1):
            for j in range(colS, colE + 1):
                if target == matrix[i][j]:
                    return True

        return False

    def searchMatrix(self, matrix, target):

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        rowS = 0
        colE = n - 1

        while rowS < m and colE >= 0:
            if matrix[rowS][colE] == target:
                return True
            elif target > matrix[rowS][colE]:
                rowS += 1
            else:
                colE -= 1

        return False

if __name__ == "__main__":
    m = int(input())
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().strip().split(","))))

    target = int(input())
    s = Solution().searchMatrix(arr, target)
    print(s)
