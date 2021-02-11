def moveElementToEnd(array: list, to_move: int):
    collect_list = list()
    for i in array:
        if i != to_move:
            collect_list.append(i)
    collect_list.sort()
    moved_list = collect_list + [to_move] * (len(array) - len(collect_list))
    return moved_list


if __name__ == "__main__":
    arr = [2, 1, 2, 2, 2, 3, 4, 2]
    to_move = 2
    moved_list = moveElementToEnd(arr, to_move)
    print(moved_list)
