# Name: QuickSort3.py
# Author: Charles Carter
# Date: May 3, 2022
# Purpose: implement the Quicksort algorithm
 
###begin enable DEBUG mode###
"""
This is not part of quicksort
the following lines enable DEBUG mode if
passed a parameter on the command line
"""
import sys
DEBUG = 0
if (len(sys.argv) > 1):
    DEBUG = 1
    print("DEBUG is TRUE")
###end enable DEBUG mode###
 
###begin quicksort implementation### 
def quick_sort(arr):
    if DEBUG: print(f"calling quick_sort({arr})")
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        if DEBUG: print(f"    DONE if list length <= 1, returning {arr}")
        return arr
    else:
        if DEBUG: print(f"    else branch, list is {arr}")
        pivot = arr[(len(arr)-1) // 2]
        for i in arr:
            if DEBUG: print(f"       for: i = {i} and pivot = {pivot},", end = '')
            if i < pivot:           
                less.append(i)
                if DEBUG: print(f" i < pivot, less = {less}")
            elif i > pivot:
                more.append(i)
                if DEBUG: print(f" i > pivot, more = {more}")
            else:
                pivotList.append(i)
                if DEBUG: print(f" i == pivot, pivotList = {pivotList}")
        less = quick_sort(less)
        more = quick_sort(more)
        if DEBUG: print(f"<<<returning {less} + {pivotList} + {more}")
        return less + pivotList + more
   
###testing quicksort implementation### 
if __name__ == '__main__':
    x = [4,3,7,2,9,5,99,-1]
    print(f"initial list is {x}")
    x1 = quick_sort(x)
    print(f"end list is {x1}")
    print()
    #y = list('Hello World!')
    y = list('qwerty')
    print(f"initial list is {y}")
    y1 = quick_sort(y)
    print(f"end list is {y1}")
