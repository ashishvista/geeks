# User function Template for python3

def qPush(x, stack1, stack2):


    for i in range(len(stack1)):
        stack2.append(stack1.pop())

    stack2.append(x)

    for i in range(len(stack2)):
        stack1.append(stack2.pop())


def qPop(stack1, stack2):
    if len(stack1) > 0:
       return stack1.pop()
    else:
        return -1




if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry = int(input())
        qtyp_qry = list(map(int, input().strip().split()))

        i = 0
        stack1 = []
        stack2 = []
        while i < len(qtyp_qry):
            # print(i)
            if qtyp_qry[i] == 1:
                qPush(qtyp_qry[i + 1], stack1, stack2)
                # print(i)
                i += 2
            else:
                print(qPop(stack1, stack2), end=' ')
                i += 1

        print()
# } Driver Code Ends
