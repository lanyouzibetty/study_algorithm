import os


def findSmallestElemIdx(alist):
    smallest_elem = alist[0]
    smallest_idx = 0
    for i in range(1, len(alist)):
        if alist[i] < smallest_elem:
            smallest_elem = alist[i]
            smallest_idx = i
    return smallest_idx


def findBiggestElemIdx(alist):
    biggest_elem = alist[0]
    biggest_idx = 0
    for i in range(1, len(alist)):
        if alist[i] > biggest_elem:
            biggest_elem = alist[i]
            biggest_idx = i
    return biggest_idx


find_idx = {"ascend": findSmallestElemIdx,
            "descend": findBiggestElemIdx}


def selectionSort(alist, mode="ascend"):
    out_list = []
    for i in range(len(alist)):
        selected_idx = find_idx[mode](alist)
        out_list.append(alist.pop(selected_idx))
    return out_list


if __name__ == "__main__":
    test_list = [4, 6, 9, 1, 3, 2]
    print("orignal:", test_list)
    print("ascend:", selectionSort(test_list.copy()))
    print("descend:", selectionSort(test_list.copy(), mode="descend"))
