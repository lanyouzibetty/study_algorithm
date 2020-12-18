import os
import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    base_item = random.choice(arr)
    less_base = [item for item in arr if item < base_item]
    bigger_base = [item for item in arr if item > base_item]
    return quick_sort(less_base) + [base_item] + quick_sort(bigger_base)
    

if __name__=="__main__":
    a = [1, 3, 9, 7, 5, 6]
    print("origin arr:", a)
    print("quick sorted:", quick_sort(a))