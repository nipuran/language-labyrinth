def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[high], array[i+1] = array[i+1], array[high]
    return i + 1



def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, high)


test_1 = [1,2,3,4,5,6]
test_2 = [8, 3, 1, 7, 0, 10, 2]
test_3 = [1]
test_4 = []

quickSort(test_1, 0, len(test_1)-1)
quickSort(test_2, 0, len(test_2)-1)
quickSort(test_3, 0, len(test_3)-1)
quickSort(test_4, 0, len(test_4)-1)
print(test_1)
print(test_2)
print(test_3)
print(test_4)
