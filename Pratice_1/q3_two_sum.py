def two_sum(nums, tar):
    d = {}

    for i in range(len(nums)):
        x = nums[i]
        need = tar - x

        if need in d:
            return [d[need], i]

        d[x] = i

    return []


nums = [2, 7, 11, 15]
tar = 9

print(two_sum(nums, tar))
