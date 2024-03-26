"""
     Optimal Merge Algorithm
Receive k element to be merged
Sorted them all
Look at the size of each one before merging, we starting with the smallest one
until we merge them all
"""

def merge_sort(arr, low, high):
    if low < high:
        middle = int((low + high) / 2)
        merge_sort(arr, low, middle)
        merge_sort(arr, middle + 1, high)
        return merge(arr, low, middle, high)

def merge(arr, low, middle, high):
    i = 0
    j = 0
    k = low

    left = arr[low:middle+1]
    right = arr[middle+1:high+1]

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # adding the rest of the sorted array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


    return arr

def merge_and_sort(*arrays):
    sorted = []
   
    i = 0
    j = 0
    # sorted each array individually and add to a mother array
    for array in arrays:
        merge_sort(array, 0, len(array) - 1)
        sorted.append(array)
    
    # sorted array by size

    for n in range(len(sorted) - 1):

        while n >= 0 and len(sorted[n]) > len(sorted[n+1]):
            sorted[n], sorted[n+1] = sorted[n+1], sorted[n]
            n -= 1

    # optimal merge
    merged = []

    for n in range(len(sorted)):
        if n > 0:
            break
        
        merged.extend(sorted[n])
        merged.extend(sorted[n+1])
        merge_sort(merged, 0, len(merged) - 1)

        for i in range(2, len(sorted)):
            merged.extend(sorted[i])
            merge_sort(merged, 0, len(merged) - 1)

    return merged


def main():
    a = [5, 9, 0, 1, 11, 7, 3]
    b = [1, 5, 9, 2, 0, 4, 11, 16, 13]
    c = [6, 3, 9, 0, 2]
    d = [7, 11, 4, 8, 0, 16]
    e = [9, 3, 6, 5, 1, 2, 4, 8, 10, 12]
    result = merge_and_sort(a, b, c, d, e)
    print(result)


if __name__ == '__main__':
    main()