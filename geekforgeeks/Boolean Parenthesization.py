import sys

sys.setrecursionlimit(10 ** 6)


def parenthesization(w):
    return parenthesizationUtil(w, 0, len(w) - 1, True)


def parenthesizationUtil(w, s, e, bool):
    global dp_h
    if dp_h[bool][s][e] > -1:
        return dp_h[bool][s][e]
    tmp = w[s:e + 1]
    # if tmp == "T&F^T" and bool:
    #     print()
    if e == s:
        if w[e] == "T" and bool:
            return 1
        elif w[e] == "F" and not bool:
            return 1
        else:
            return 0

    start = s
    mid = s + 1
    end = e
    count = 0
    while mid < end:
        if w[mid] == "&":
            if bool:
                l = parenthesizationUtil(w, start, mid - 1, True)
                r = parenthesizationUtil(w, mid + 1, end, True)

                if l > 0 and r > 0:
                    count += l * r

            else:
                l = parenthesizationUtil(w, start, mid - 1, False)
                r = parenthesizationUtil(w, mid + 1, end, False)

                if l > 0 and r > 0:
                    count += l * r

                l = parenthesizationUtil(w, start, mid - 1, True)
                r = parenthesizationUtil(w, mid + 1, end, False)

                if l > 0 and r > 0:
                    count += l * r

                l = parenthesizationUtil(w, start, mid - 1, False)
                r = parenthesizationUtil(w, mid + 1, end, True)

                if l > 0 and r > 0:
                    count += l * r



        elif w[mid] == "|":
            if bool:
                l = parenthesizationUtil(w, start, mid - 1, True)
                r = parenthesizationUtil(w, mid + 1, end, False)

                if l > 0 and r > 0:
                    count += l * r

                l = parenthesizationUtil(w, start, mid - 1, False)
                r = parenthesizationUtil(w, mid + 1, end, True)

                if l > 0 and r > 0:
                    count += l * r

                l = parenthesizationUtil(w, start, mid - 1, True)
                r = parenthesizationUtil(w, mid + 1, end, True)

                if l > 0 and r > 0:
                    count += l * r

            else:
                l = parenthesizationUtil(w, start, mid - 1, False)
                r = parenthesizationUtil(w, mid + 1, end, False)

                if l > 0 and r > 0:
                    count += l * r

        elif w[mid] == "^":
            if bool:
                l = parenthesizationUtil(w, start, mid - 1, True)
                r = parenthesizationUtil(w, mid + 1, end, False)

                if l > 0 and r > 0:
                    count += l * r

                l = parenthesizationUtil(w, start, mid - 1, False)
                r = parenthesizationUtil(w, mid + 1, end, True)

                if l > 0 and r > 0:
                    count += l * r

            else:
                l = parenthesizationUtil(w, start, mid - 1, True)
                r = parenthesizationUtil(w, mid + 1, end, True)

                if l > 0 and r > 0:
                    count += l * r

                l = parenthesizationUtil(w, start, mid - 1, False)
                r = parenthesizationUtil(w, mid + 1, end, False)

                if l > 0 and r > 0:
                    count += l * r

        mid += 2
    # if tmp == "T&F^T":
    #     print(count)
    dp_h[bool][s][e] = count % 1003
    return dp_h[bool][s][e]


def parenthesization2(w):
    start = 0
    size = 1
    exp_length = size + (size - 1)
    end = len(w) - 1
    word_length = len(w)
    global dp_h
    while exp_length <= word_length:
        while start <= word_length - exp_length:
            s = start
            e = start + exp_length - 1
            dp_h[True][s][e] = parenthesizationUtil2(w, s, e, True)
            dp_h[False][s][e] = parenthesizationUtil2(w, s, e, False)
            start += 2
        start = 0
        size += 1
        exp_length = size + (size - 1)

    tmp = dp_h
    return dp_h[True][0][word_length - 1]


def parenthesizationUtil2(w, s, e, bool):
    global dp_h

    tmp = w[s:e + 1]
    if e == s:
        if w[e] == "T" and bool:
            return 1
        elif w[e] == "F" and not bool:
            return 1
        else:
            return 0

    start = s
    mid = s + 1
    end = e
    count = 0
    while mid < end:
        ls = start
        le = mid - 1
        rs = mid + 1
        re = end
        if w[mid] == "&":
            if bool:
                l = dp_h[True][ls][le]
                r = dp_h[True][rs][re]

                if l > 0 and r > 0:
                    count += l * r

            else:
                l = dp_h[False][ls][le]
                r = dp_h[False][rs][re]

                if l > 0 and r > 0:
                    count += l * r

                l = dp_h[True][ls][le]
                r = dp_h[False][rs][re]

                if l > 0 and r > 0:
                    count += l * r

                l = dp_h[False][ls][le]
                r = dp_h[True][rs][re]

                if l > 0 and r > 0:
                    count += l * r

        elif w[mid] == "|":
            if bool:
                l = dp_h[True][ls][le]
                r = dp_h[False][rs][re]

                if l > 0 and r > 0:
                    count += l * r

                l = dp_h[False][ls][le]
                r = dp_h[True][rs][re]

                if l > 0 and r > 0:
                    count += l * r

                l = dp_h[True][ls][le]
                r = dp_h[True][rs][re]

                if l > 0 and r > 0:
                    count += l * r

            else:

                l = dp_h[False][ls][le]
                r = dp_h[False][rs][re]

                if l > 0 and r > 0:
                    count += l * r

        elif w[mid] == "^":
            if bool:
                l = dp_h[True][ls][le]
                r = dp_h[False][rs][re]
                if l > 0 and r > 0:
                    count += l * r

                l = dp_h[False][ls][le]
                r = dp_h[True][rs][re]
                if l > 0 and r > 0:
                    count += l * r

            else:
                l = dp_h[True][ls][le]
                r = dp_h[True][rs][re]
                if l > 0 and r > 0:
                    count += l * r

                l = dp_h[False][ls][le]
                r = dp_h[False][rs][re]
                if l > 0 and r > 0:
                    count += l * r

        mid += 2
    # if tmp == "T&F^T":
    #     print(count)
    return count % 1003


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        w = input()
        dp1 = [[-1 for i in range(len(w))] for i in range(len(w))]
        dp2 = [[-1 for i in range(len(w))] for i in range(len(w))]
        dp_h = {True: dp1, False: dp2}

        # if t==0:
        #     print(0)
        #     break
        res = parenthesization2(w)
        print(res)
