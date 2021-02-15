if __name__ == "__main__":
    arr = []
    h = {}
    with open("/downloads/redis_keys2.txt", 'r', encoding='utf-8') as f:
        arr = f.readlines()
    count = 0
    for line in arr:
        count += 1
        tmp = line[:9]
        if tmp in h:
            h[tmp] += 1
        else:
            h[tmp] = 1

    sorted_x = sorted(h.items(), key=lambda kv: kv[1],reverse=True)

    print(h)

# file1 = open("/home/ashish/PycharmProjects/geeks/downloads/redis_keys.txt", "r")
# print(file1.readlines())
# file1.close()
