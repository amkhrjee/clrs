sum = maxLow = maxHigh = 0


def find_max_sublist(list):
    maxSum = -999
    for i in range(len(list)):
        sum = 0
        for j in range(i, len(list)):
            sum = sum + list[j]
            if(sum > maxSum):
                maxSum = sum
                maxLow = i
                maxHigh = j
    return (maxSum, maxLow, maxHigh)


list = [4, -6, 3, 57, -8, 34, -67, 37, -91, 5]
(sum, low, high) = find_max_sublist(list)
print('Max sum:', sum, '\nList:', list[low:high+1])
