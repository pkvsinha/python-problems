#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

class Window:
    def __init__(self, maxv, arr=[]):
        self.size = len(arr)
        self.queue = deque()
        self._count = [0] * (maxv + 1)
        for e in arr:
            self._count[e] += 1
            self.queue.append(e)

    def add(self, n):
        self.queue.append(n)
        self._count[n] += 1
        val = self.queue.popleft()
        self._count[val] -= 1

    def median(self):
        if self.size % 2 == 0:
            mid = (self.size // 2) + 1
            c = 0
            p = None
            i = 0
            for num in self._count:
              if (c + num) >= mid:
                if p == None:
                  return i
                else:
                  return (p + i) / 2
              elif (c + num) == (mid - 1):
                p = i
              c += num
              i += 1
        else:
            mid = ((self.size - 1) // 2 ) + 1
            i = 0
            while mid > 0:
                if self._count[i] == 0:
                    i += 1
                else:
                    if self._count[i] >= mid:
                        return i
                    else:
                        mid -= self._count[i]
                        i += 1

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    n = len(expenditure)
    if n <= d:
        return 0
    else:
        w = Window(201, expenditure[:d])
        noti_count = 0
        for i in range(d, n):
            if expenditure[i] >= 2 * w.median():
                noti_count += 1
            w.add(expenditure[i])
            x += 1
        return noti_count

if __name__ == '__main__':
    f = open('C:\\Users\\prashant.s\\Desktop\\data.txt', 'r')

    nd = f.readline().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, f.readline().rstrip().split()))

    f.close()
    
    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
