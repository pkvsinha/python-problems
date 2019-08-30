#!/bin/python3

import math
import os
import random
import re
import sys

def counter():
    count = 0
    def inc(i=None):
        nonlocal count
        if i == None:
            return count
        count += i
    return inc

def merge(A, lo, mid, hi, counter):
    arr = [0] * ((hi-lo) + 1)
    i = lo
    j = mid+1
    k = 0
    while i <= mid and j <= hi:
        if A[i] <= A[j]:
            arr[k] = A[i]
            i += 1
        else:
            arr[k] = A[j]
            counter(mid-i+1)
            j += 1
        k += 1
    if i <= mid:
        for p in range(i, mid+1):
            arr[k] = A[p]
            k += 1
    if j <= hi:
        for p in range(j, hi+1):
            arr[k] = A[p]
            k += 1
    k = lo
    for v in arr:
        A[k] = v
        k += 1

def merge_sort(A, lo, hi, counter):
    if lo < hi:
        mid = (lo+hi) // 2
        merge_sort(A, lo, mid, counter)
        merge_sort(A, mid+1, hi, counter)
        merge(A, lo, mid, hi, counter)

# Complete the countInversions function below.
def countInversions(arr):
    count_fn = counter()
    merge_sort(arr, 0, len(arr) - 1, count_fn)
    return count_fn()

if __name__ == '__main__':
    f = open('.\\data.txt', 'r')
    t = int(f.readline())
    for t_itr in range(t):
        n = int(f.readline())

        arr = list(map(int, f.readline().rstrip().split()))

        result = countInversions(arr)

        print(str(result))
    f.close()

