def max_families(n, m, seats_arr, hash):
    arr = [[1 for i in range(9)] for i in range(n)]  ## 1 means vacant and 0 means occupied
    for seat in seats_arr:
        l = len(seat)
        row = int(seat[0:l - 1])
        col = hash[seat[l - 1]]
        # print(row, "  and  ", col)
        arr[row - 1][col] = 0

    c = 0
    for i in range(n):
        if arr[i][1] and arr[i][2] and arr[i][3] and arr[i][4]:
            arr[i][1] = arr[i][2] = arr[i][3] = arr[i][4] = 0   ## make all these seat occupied
            c = c + 1
        if arr[i][3] and arr[i][4] and arr[i][5] and arr[i][6]:
            arr[i][3] = arr[i][4] = arr[i][5] = arr[i][6] = 0  ## make all these seat occupied
            c = c + 1
        if arr[i][5] and arr[i][6] and arr[i][7] and arr[i][8]:
            arr[i][5] = arr[i][6] = arr[i][7] = arr[i][8] = 0  ## make all these seat occupied
            c = c + 1
    print(c)


if __name__ == "__main__":
    tcases = int(input())
    n = int(input())  # number of rows
    m = int(input())  # seats_arr length
    seats_arr = []
    reserved_seats = input()
    if m > 0:
        seats_arr = reserved_seats.strip().split(" ")
    hash = {  ### conversion of seat alphatbets to column number
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "J": 8,
        "K": 9
    }
    # print(n, m, seats_arr)

    max_families(n, m, seats_arr, hash)
