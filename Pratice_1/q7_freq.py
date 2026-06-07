def most_freq(lst):
    if len(lst) == 0:
        return None

    d = {}
    ans = lst[0]
    cnt = 0

    for x in lst:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1

        if d[x] > cnt:
            cnt = d[x]
            ans = x

    return ans


a = [4, 1, 2, 2, 3, 3, 3, 4]

print(most_freq(a))
