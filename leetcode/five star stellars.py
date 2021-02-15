def fiveStarReviews(productRatings, ratingThreshold):
    r = len(productRatings)  #rows
    adfr = 0  #additional reviews needed

    while True:
        currentAvgRating = getCurrentThresholds(productRatings, r)
        if currentAvgRating >= ratingThreshold:
            return adfr
        else:
            index = getDiffMaxIndex(productRatings, r)
            productRatings[index][0] = productRatings[index][0] + 1
            productRatings[index][1] = productRatings[index][1] + 1
            adfr += 1


def getCurrentThresholds(pr, r):
    c = 0
    for i in range(r):
        c += pr[i][0] / pr[i][1]

    return c / r * 100


def getDiffMaxIndex(pr, r):
    maxDiff = float("-inf")
    maxDiffIndex = 0
    for i in range(r):
        tmp = ((pr[i][0] + 1) / (pr[i][1] + 1)) - (pr[i][0] / pr[i][1])
        if tmp > maxDiff:
            maxDiffIndex = i
            maxDiff = tmp

    return maxDiffIndex


if __name__ == "__main__":
    r = int(input().strip())
    c = int(input().strip())
    arr = []

    for i in range(r):
        tmp = list(map(int, input().strip().split()))
        arr.append(tmp)

    ratingThreshold = int(input().strip())
    res = fiveStarReviews(arr, ratingThreshold)
    print(res)
