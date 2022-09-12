# Name: merge_sort.py
# Author: Charles Carter
# Date: September 11, 2022
# Purpose: implementaton of mergesort algorithm

###begin enable DEBUG mode###
"""
This is not part of mergesort
the following lines enable DEBUG mode if
passed a parameter on the command line
"""
import sys
DEBUG = 0
if (len(sys.argv) > 1):
    DEBUG = 1
    print("DEBUG is TRUE") 
###begin mergesort implementation### 
def merge_sort(array):
    if DEBUG == 1: print(f"calling merge_sort({array})")
    if len(array) > 1:

        #  mid is the point where the array is divided into two subarrays
        mid = len(array)//2
        Left = array[:mid]
        Right = array[mid:]
        if DEBUG:
            print(f"middle index is {mid}, middle element is {array[mid]}")
            print(f"2. {Left}")
            print(f"3. {Right}")

        # Sort the two halves
        merge_sort(Left)
        merge_sort(Right)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        if DEBUG: print(f"     merging Left and Right")
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1

        # When we run out of elements in either Left or Right,
        # pick up the remaining elements and put in A[p..r]
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1

        if DEBUG: print(f"     merged array so far is f{array}")




# Driver program
if __name__ == '__main__':
    x = [4,3,7,2,9,5,99,-1]
    print(f"initial list is {x}")
    merge_sort(x)
    print(f"end list is {x}")
    print()

    y = list('qwerty')
    print(f"initial list is {y}")
    merge_sort(y)
    print(f"end list is {y}")
