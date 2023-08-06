def twosum(target, arr):

    map = {}
    for i, num in enumerate(len(arr)):

        diff = target - num
        if diff in map:
            return [i, num]
        map[i] = num


arr = [5, 1, 2, 6, 3]

twosum(arr, 7)
