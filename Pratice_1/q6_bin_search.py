def bsearch(arr, tar):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == tar:
            return mid

        if arr[mid] < tar:
            l = mid + 1
        else:
            r = mid - 1

    return -1


a = [1, 3, 5, 7, 9, 11]

print(bsearch(a, 7))
print(bsearch(a, 4))
