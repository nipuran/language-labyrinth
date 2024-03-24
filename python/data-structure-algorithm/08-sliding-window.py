# Example 3: 713. Subarray Product Less Than K.

# Given an array of positive integers nums and an integer k, return the number of subarrays where the 
# product of all the elements in the subarray is strictly less than k.

# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with 
# products less than k are:

# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

def func(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0
    left = ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1
    return ans


def main():
    nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    k = 19
    print(func(nums, k))

if __name__ == '__main__':
    main()
