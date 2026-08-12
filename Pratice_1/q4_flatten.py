def flat(lst):
    ans = []

    for x in lst:
        if isinstance(x, list):
            small = flat(x)
            for y in small:
                ans.append(y)
        else:
            ans.append(x)

    return ans


if __name__ == "__main__":
    print(flat([[1, [2, 3]], [4, [5, [6]]]]))
