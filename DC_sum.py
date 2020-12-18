import os


def DC_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + DC_sum(arr[1:])

def DC_count(arr):
    if arr == []:
        return 0
    else:
        return 1 + DC_count(arr[1:])

def DC_max(arr):
    if arr == []:
        print("the arr is empty !!!")
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = DC_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


if __name__=="__main__":
    a = [1, 2, 3, 4]
    print(DC_sum(a))
    print(DC_count(a))
    print(DC_max(a))