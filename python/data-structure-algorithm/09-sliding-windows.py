# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest 
# sum whose length is k.

def numSubarrayLargestSumLenK(nums: list[int], k: int) -> int:
    left = curr = 0

    for right in range(k):
        curr += nums[right]
        print(f'{nums[left:right+1]}={curr}')

    total = curr

    for right in range(k, len(nums)):
        curr += nums[right]
        curr -= nums[right - k]
        left += 1
        print(f'{nums[left:right+1]}={curr}')
        total = max(total, curr)

    return total

def main():
    nums = [3, -1, 4, 12, -8, 5, 5]
    k = 4
    print(numSubarrayLargestSumLenK(nums, k))

if __name__ == '__main__':
    main()
