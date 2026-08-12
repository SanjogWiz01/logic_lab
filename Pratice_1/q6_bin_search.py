def bsearch(arr, tar):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == tar:
            return mid

        if arr[mid] < tar:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    values = [1, 3, 5, 7, 9, 11]
    print(bsearch(values, 7))
    print(bsearch(values, 4))
