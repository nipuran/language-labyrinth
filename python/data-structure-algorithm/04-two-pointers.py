# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array 
# that combines both of them and is also sorted.

def combineArray(arr1, arr2):
    i, j = 0, 0

    newArr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newArr.append(arr1[i])
            i += 1
        else:
            newArr.append(arr2[j])
            j += 1

    while i < len(arr1):
        print('looping arr1 again..')
        newArr.append(arr1[i])
        i += 1

    while j < len(arr2):
        print('looping arr2 again..')
        newArr.append(arr2[j])
        j += 1

    return newArr

    

def main():
    arr1 = [1, 3, 4, 7, 8]
    arr2 = [2, 5, 6, 9]
    print(combineArray(arr1, arr2))

if __name__ == '__main__':
    main()
