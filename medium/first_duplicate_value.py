def firstDuplicateValue(array):
    queue_list = list()
    for i in array:
        if i in queue_list:
            return i
        else:
            queue_list.append(i)
    return -1


if __name__ == '__main__':
    arr = [2, 1, 5, 2, 3, 3, 4]
    print(firstDuplicateValue(arr))
