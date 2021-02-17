def is_monotonic(arr: list):
    for i in range(0, len(arr)):
        pre_idx = i
        if i + 1 < len(arr) - 1:
            next_idx = i + 1
        else:
            break
        if arr[next_idx] > arr[pre_idx]:
            return False
    return True


if __name__ == "__main__":
    l = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    print(is_monotonic(l))
