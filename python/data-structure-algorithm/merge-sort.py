def merge(left, right):
    left_pointer, right_pointer = 0, 0
    sorted_array = []

    while (left_pointer < len(left) and right_pointer < len(right)):
        if left[left_pointer] < right[right_pointer]:
            sorted_array.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_array.append(right[right_pointer])
            right_pointer += 1

    while left_pointer < len(left):
        sorted_array.append(left[left_pointer])
        left_pointer += 1

    while right_pointer < len(right):
        sorted_array.append(right[right_pointer])
        right_pointer += 1

    return sorted_array

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


test_1 = mergeSort([1,2,3,4,5,6])
test_2 = mergeSort([8, 3, 1, 7, 0, 10, 2])
test_3 = mergeSort([1])
test_4 = mergeSort([])

print(test_1)
print(test_2)
print(test_3)
print(test_4)

            
