#insertion sort in ascending order (int)
def insertSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and  A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key

A = [5, 7, -8, 9, 10,12, 4, -7, 0,-12, 1, 6, 2, 3, -4, -15]
insertSort(A)
print(A)
#insertion sort in descending order (int)
def insertSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and  key > A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key

        
A = [5, 7, -8, 9, 10,12, 4, -7, 0,-12, 1, 6, 2, 3, -4, -15]
insertSort(A)
print(A)