from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def merge_sort(arr):
    if len(arr) == 1:
        return None

    mid = len(arr)//2
    arr_l = arr[:mid]
    arr_r = arr[mid:]
    arr.clear()

    merge_sort(arr_l)
    merge_sort(arr_r)

    pos_l = 0
    pos_r = 0

    while pos_l != len(arr_l) and pos_r != len(arr_r):
        if arr_l[pos_l] <= arr_r[pos_r]:
            arr.append(arr_l[pos_l])
            pos_l += 1
            continue

        if arr_l[pos_l] > arr_r[pos_r]:
            arr.append(arr_r[pos_r])
            pos_r += 1
            continue

    while pos_l != len(arr_l):
        arr.append(arr_l[pos_l])
        pos_l += 1

    while pos_r != len(arr_r):
        arr.append(arr_r[pos_r])
        pos_r += 1

    return None


n, s = map(int, input().split())
array = list(map(int, input().split()))

merge_sort(array)

if s == 1:
    array = reversed(array)

print(*array, sep= " ")
