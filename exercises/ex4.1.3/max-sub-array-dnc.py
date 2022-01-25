import math


def find_max_crossing_subarray(list, low, mid, high):
    left = low
    right = high
    leftSum = 0
    rightSum = 0
    sum = 0
    for i in reversed(range(low, mid)):
        sum += list[i]
        if sum > leftSum:
            leftSum = sum
            left = i
    sum = 0
    for j in range(mid, high):
        sum += list[j]
        if sum > rightSum:
            rightSum = sum
            right = j
    return (left, right, leftSum + rightSum)


def find_max_subarray(list, low, high):
    if low == high:
        return (low, high, list[low])
    else:
        mid = (low + high) // 2
        (leftLow, leftHigh, leftSum) = find_max_subarray(list, low, mid)
        (rightLow, rightHigh, rightSum) = find_max_subarray(list, mid + 1, high)
        (crossLow, crossHigh, crossSum) = find_max_crossing_subarray(
            list, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)
        if rightSum >= leftSum and rightSum >= crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)


list = [-4, -6, -3, -57, -8, -34, -67, -37, -91, -5]
(left, right, sum) = find_max_subarray(list, 0, len(list) - 1)
print('Sum:', sum, '\nList:', list[left:right+1])
