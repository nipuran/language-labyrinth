# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of 
# numbers that sum to target, false otherwise. This problem is similar to Two Sum. 
# (In Two Sum, the input is not sorted).
#
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.


def func(arr, target) -> bool:
    left = 0
    right = len(arr) - 1

    while left < right:

        pairSum: int = (arr[left] + arr[right])

        if pairSum == 13:
            return True

        if pairSum > 13:
            right -= 1
        else:
            left += 1

    return False

def main():
    nums = [1, 2, 4, 6, 8, 9, 14, 15]
    print(func(nums, 13))

if __name__ == '__main__':
    main()
