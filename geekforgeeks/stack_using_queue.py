# User function Template for python3

def push_in_stack(x):
    # global declaration
    global queue_1  # pop purpose
    global queue_2  # push purpose

    queue_2.append(x)

    length = len(queue_1)
    for i in range(length):
        item = queue_1.pop(0)
        queue_2.append(item)

    temp = queue_2
    queue_2 = queue_1
    queue_1 = temp
    # code here


def pop_from_stack():
    # global declaration
    global queue_1
    global queue_2

    if len(queue_1) > 0:
        item = queue_1.pop(0)
        return item
    else:
        return -1
    # code here


queue_1 = []  # first queue  //main q
queue_2 = []  # second queue /// secondary q  for push purpose

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        while i < len(a):
            if a[i] == 1:
                push_in_stack(a[i + 1])
                i += 1
            else:
                print(pop_from_stack(), end=" ")
            i += 1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
