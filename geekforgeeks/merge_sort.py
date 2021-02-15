# User function Template for python3

def mergeSort(arr):
    new_arr = divide(arr, 0, len(arr) - 1)
    for i in range(len(new_arr)):
        arr[i] = new_arr[i]


def divide(arr, low, high):
    if low == high:
        return [arr[low]]
    mid = int((low + high) / 2)
    sub1 = divide(arr, low, mid)
    sub2 = divide(arr, mid + 1, high)
    sub3 = []
    sub1_len = len(sub1)
    sub2_len = len(sub2)
    i = j = 0
    while i < sub1_len and j < sub2_len:
        if sub1[i] <= sub2[j]:
            sub3.append(sub1[i])
            i += 1
        else:
            sub3.append(sub2[j])
            j += 1
    while i < sub1_len:
        sub3.append(sub1[i])
        i += 1
    while j < sub2_len:
        sub3.append(sub2[j])
        j += 1
    return sub3


# add code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mergeSort(arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends

