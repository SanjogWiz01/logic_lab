def grp(words):
    d = {}

    for w in words:
        k = "".join(sorted(w))

        if k in d:
            d[k].append(w)
        else:
            d[k] = [w]

    ans = []
    for k in d:
        ans.append(d[k])

    return ans


wds = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(grp(wds))
