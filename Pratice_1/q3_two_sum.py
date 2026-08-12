def two_sum(nums, tar):
    """Return indices of the first pair adding to ``tar``, or ``[]``."""
    d = {}

    for i in range(len(nums)):
        x = nums[i]
        need = tar - x

        if need in d:
            return [d[need], i]

        d[x] = i

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
