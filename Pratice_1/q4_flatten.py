def flat(lst):
    ans = []

    for x in lst:
        if type(x) == list:
            small = flat(x)
            for y in small:
                ans.append(y)
        else:
            ans.append(x)

    return ans


a = [[1, [2, 3]], [4, [5, [6]]]]

print(flat(a))
