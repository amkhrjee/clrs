import time

# merge sort


def merge_sort(list):
    list_length = len(list)
    if list_length == 1:
        return list
    midpoint = list_length // 2
    left_list = merge_sort(list[:midpoint])
    right_list = merge_sort(list[midpoint:])

    return merge(left_list, right_list)


def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output


def run_merge_sort():
    unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
    print('Unsorted list:', unsorted_list)
    print('Sorted List:', merge_sort(unsorted_list))


t0 = time.perf_counter()
run_merge_sort()
t1 = time.perf_counter()
print('Time taken', (t1 - t0), 'seconds')

# insertionsort


def insertion_sort(list):
    if len(list) == 1:
        return list
