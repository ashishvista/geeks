def stockspan(n, arr):
    stock = [-1 for i in range(n)]
    stock[0] = 1
    for i in range(1, n):
        stock[i] = stockspanUtil(i, arr, stock)

    for i in range(n):
        print(stock[i], end=" ")


def stockspanUtil(i, arr, stock):
    span = 1
    j = i - 1
    while j >= 0 and arr[i] >= arr[j]:
        tmp = stock[j]
        span = span + tmp
        j = j - tmp
    return span


def stockspan2(n, arr):
    stock = [-1 for i in range(n)]
    stock[0] = 1
    st = [0]
    for i in range(1, n):
        while st:
            if arr[i] >= arr[st[-1]]:
                st.pop()
            else:
                break
        if not st:
            stock[i] = i + 1
        else:
            stock[i] = i - st[-1]
        st.append(i)

    for i in range(n):
        print(stock[i], end=" ")

if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stockspan2(n, arr)
        print()
