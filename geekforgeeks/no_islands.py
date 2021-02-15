# User function Template for python3
'''
	Your task is to return the count of number
	of islands in the given boolean grid.

	Function Arguments: a (boolean grid), n -> no of rows, m -> no of columns.
	Return Type: Integer

	Contributed By: Nagendra Jha
'''

# importing the sys module
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10 ** 6)

def findIslands(a, n, m):
    visited = [[False for i in range(m)] for j in range(n)]
    count = 0
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and a[r][c] == 1:
                count = count + 1
                try:
                    dfs(r, c, a, n, m, visited)
                except Exception as e:
                    print(e)
                    return count
    print(visited)
    return count


def dfs(r, c, a, n, m, visited):
    visited[r][c] = True
    rN = [-1, -1, -1,  0, 0,  1, 1, 1]
    cN = [-1,  0,  1, -1, 1, -1, 0, 1]

    for i in range(8):
        p = r + rN[i]
        q = c + cN[i]
        if isSafe(p, q, n, m, a) and not visited[p][q] and a[r][c] == 1:
            dfs(p, q, a, n, m, visited)


def isSafe(i, j, n, m, a):
    if i >= 0 and i < n and j >= 0 and j < m:
        return True
    else:
        return False


# code here

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, m = map(int, input().strip().split())
        cell_info = list(map(int, input().strip().split()))
        a = []
        k = 0  # current index
        # create the boolean matrix from cell information
        for i in range(n):
            row_i = []
            for j in range(m):
                row_i.append(cell_info[k])
                k += 1
            a.append(row_i)
        print(findIslands(a, n, m))
# } Driver Code Ends
