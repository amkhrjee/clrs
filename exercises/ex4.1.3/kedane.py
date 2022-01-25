import math


def find_max_subarray(arr):
    sum = - math.inf
    tempSum = 0
    left = 0
    right = 0
    tempLeft = 0
    for i in range(len(arr)):
        tempSum += arr[i]
        if tempSum > sum:
            sum = tempSum
            left = tempLeft
            right = i
        elif tempSum < 0:
            tempSum = 0
            tempLeft = i + 1
    return (sum, left, right)


list = [4, 6, -3, 57, -8, -34, -67, 37, -91, -5]
(sum, left, right) = find_max_subarray(list)
print('Sum:', sum, '\nList:', list[left:right+1])
