def take_input():
    tcases = int(input())
    matrix = []
    for tcase in range(tcases):
        rows, cols = list(map(int, input().strip().split()))
        raw_matrix = list(map(int, input().strip().split()))
        k = 0
        for row in range(rows):
            arr = []
            for col in range(cols):
                arr.insert(col, raw_matrix[k])
                k = k + 1
            matrix.insert(row, arr)
        t = find_time_taken_to_rot_oranges(matrix, rows, cols)
        print(t)


def find_time_taken_to_rot_oranges(matrix, rows, cols):
    visited = [[False for r in range(cols)] for c in range(rows)]
    # print(matrix, visited)
    q = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 2:
                q.append([i, j])
                visited[i][j] = True
    if len(q) == 0:
        return 0
    q.append([-1, -1])  # adding delimiter

    k = 0
    flag = True
    while len(q) > 0:
        index = q.pop(0)
        if can_get_rotten(index[0] - 1, index[1], matrix, rows, cols, visited):
            flag = False
            q.append([index[0] - 1, index[1]])

        if can_get_rotten(index[0], index[1] - 1, matrix, rows, cols, visited):
            flag = False
            q.append([index[0], index[1] - 1])

        if can_get_rotten(index[0], index[1] + 1, matrix, rows, cols, visited):
            flag = False
            q.append([index[0], index[1] + 1])

        if can_get_rotten(index[0] + 1, index[1], matrix, rows, cols, visited):
            flag = False
            q.append([index[0] + 1, index[1]])

        if index[0] == -1:
            if not flag:
                k = k + 1
                flag = True
                q.append([-1, -1])
            else:
                for m in range(rows):
                    for n in range(cols):
                        if visited[m][n]==False and matrix[m][n]==1:
                            return -1
                return k

    # print("printitn****", q)


def can_get_rotten(i, j, matrix, rows, cols, visited):
    if i >= 0 and i < rows and j >= 0 and j < cols and matrix[i][j] == 1 and visited[i][j] == False:
        visited[i][j] = True
        # print("can be rotten",i,j)
        return True
    else:
        return False

take_input()
