import math
import random
import time
# Brute force method


def find_max_sublist(list):
    sum = maxLow = maxHigh = 0
    maxSum = -math.inf
    for i in range(len(list)):
        sum = 0
    for j in range(i, len(list)):
        sum = sum + list[j]
        if(sum > maxSum):
            maxSum = sum
            maxLow = i
            maxHigh = j
    return (maxSum, maxLow, maxHigh)


# Divide and Conquer Method
def find_max_crossing_subarray(list, low, mid, high):
    left = low
    right = high
    leftSum = -math.inf
    rightSum = -math.inf
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


# Comparison
numIterations = 1000000
for inputSize in range(2, 1000):
    arr = [random.randint(-100, 100) for _ in range(inputSize)]

# Time with brute force method
start = time.perf_counter()
for _ in range(numIterations):
    bf = find_max_sublist(arr)
bfTime = time.perf_counter() - start

# Time with recursive method
start = time.perf_counter()
for _ in range(inputSize):
    rc = find_max_subarray(arr, 0, len(arr) - 1)
rcTime = time.perf_counter() - start

print('Recursive:', rcTime, '\nBruteforce:', bfTime)

if bfTime > rcTime:
    print('Crossover point:', inputSize)
else:
    print("Recursive won by a margin:", rcTime - bfTime)
