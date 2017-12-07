'''
    kadane's algoirthm
'''
import sys


def minimum_sum(array):
    min_so_far = sys.maxsize
    prefix_array = list()
    prefix_array.append(array[0])
    for i in range(len(array)-1):
        prefix_array.append(prefix_array[i] + array[i+1])

    prefix_array.sort()

    for i in range(len(prefix_array)-1):
        diff = prefix_array[i+1] - prefix_array[i]
        if diff < min_so_far:
            min_so_far = diff

    return min_so_far


n = int(input("Enter the number of elements"+'\n'))
array = list()
for x in range(n):
    number = int(input())
    array.append(number)
print(minimum_sum(array))
