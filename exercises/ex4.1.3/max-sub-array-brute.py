import math


def find_max_sublist(list):
    left = list[0]
    right = list[len(list) - 1]
    sum = -math.inf
    for i in range(len(list)):
        tempSum = 0
        for j in range(i, len(list)):
            tempSum += list[j]
            if tempSum > sum:
                sum = tempSum
                left = i
                right = j
    if sum < 0:
        sum = 0
    return (sum, left, right)


list = [-4, -6, -3, -57, -8, -34, -67, -37, -91, -5]
(sum, low, high) = find_max_sublist(list)
print('Max sum:', sum, '\nList:', list[low:high+1])
