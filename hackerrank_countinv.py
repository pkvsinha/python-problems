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

def merge(A, B, swapper):
    a = len(A)
    b = len(B)
    n = a + b
    arr = [0] * n
    for i, v in enumerate(A):
        arr[i] = v
    i = a
    for v in B:
        j = i
        while j > 0 and arr[j-1] > v:
            swapper(1)
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v
        i += 1
    return arr 

def merge_sort(A, counter):
    if len(A) == 1:
        return A
    mid = len(A) // 2
    a = merge_sort(A[:mid], counter)
    b = merge_sort(A[mid:], counter)
    return merge(a, b, counter)

# Complete the countInversions function below.
def countInversions(arr):
    swap_fn = counter()
    merge_sort(arr, swap_fn)
    return swap_fn()

if __name__ == '__main__':
    f = open('.\\data.txt', 'r')
    t = int(f.readline())
    for t_itr in range(t):
        n = int(f.readline())

        arr = list(map(int, f.readline().rstrip().split()))

        result = countInversions(arr)

        print(str(result))
    f.close()

