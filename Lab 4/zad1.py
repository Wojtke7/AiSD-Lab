import random
import time

my_list = []

my_list2 = []

for i in range(10000):
    my_list.append(random.randint(0, 10000))
    my_list2.append(random.randint(0, 10000))

left = my_list2[0]
right = my_list2[-1]


def insertionsort(A):
    for i in range(1, len(A) - 1):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x


start_time = time.time()
insertionsort(my_list)
end_time = time.time()
total_time = end_time - start_time

print(my_list)
print(f"Time: {total_time}")


def merge(A, mid):
    L = A[:mid]
    R = A[mid:]

    i = j = k = 0

    while i < len(L) and j < len(R):

        if L[i] > R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def mergesort(A, left, right):
    if left < right:
        mid = int((left + right) / 2)
        mergesort(A, left, mid)
        mergesort(A, mid + 1, right)
        merge(A, mid)


start_time = time.time()
mergesort(my_list2, left, right)
end_time = time.time()
total_time = end_time - start_time
print(my_list)
print(f"Time: {total_time}")
