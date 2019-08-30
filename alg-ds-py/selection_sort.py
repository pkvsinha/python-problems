def swap(A, i, j):
    o = A[i]
    A[i] = A[j]
    A[j] = o

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                swap(A, i, j)

def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if A[j] > A[j+1]:
                swap(A, j, j+1)
def insertion_sort(A):
    n = len(A)
    for i in range(n-1):
        p = A[i+1]
        j = i
        while p < A[j] and j >= 0:
            swap(A, j, j+1)
            j -= 1
        A[j+1] = p
        print("pass :", i, A)
if __name__ == "__main__":
    arr = [10,2,5,100,99,83,57,81,1,0]
    # selection_sort(arr)
    # bubble_sort(arr)
    insertion_sort(arr)
    print(arr)
