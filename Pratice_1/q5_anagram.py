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


if __name__ == "__main__":
    print(grp(["eat", "tea", "tan", "ate", "nat", "bat"]))
