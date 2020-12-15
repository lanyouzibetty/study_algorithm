import os


def binary_search(alist, item):
    '''
    alist must be sorted
    '''
    low = 0
    high = len(alist) - 1

    while (low <= high):
        mid = (low + high) // 2
        guess = alist[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
    return None


if __name__ == "__main__":
    test_list = [1, 3, 4, 5, 7, 8, 11]
    print(binary_search(test_list, 4))
    print(binary_search(test_list, 6))
