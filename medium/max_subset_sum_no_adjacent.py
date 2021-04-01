def max_subset_sum_no_adjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    max_sums = array[:]
    max_sums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
    return max_sums[-1]


if __name__ == '__main__':
    print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]) == 330)

