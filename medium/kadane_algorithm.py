def kadanesAlgorithm(array):
    max_ending_here = array[0]
    max_so_far = array[0]
    for i in range(1, len(array)):
        num = array[i]
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == '__main__':
    l = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    print(kadanesAlgorithm(l))
