# Example 1: Given an array of positive integers nums and an integer k, find the length of the longest 
# subarray whose sum is less than or equal to k. This is the problem we have been talking about above. 
# We will now formally solve it.

import numpy as np


def longSubArrSum(nums, k):
    left = 0
    # total sum of the current window
    curr = 0
    # length of the longest window
    answer = 0


    for right in range(len(nums)):
        curr += nums[right]
        if curr < 8:
            print(nums[left:right+1])
        elif curr == 8:
            print('↓↓↓↓↓↓↓↓↓')
            print(nums[left:right+1])
            print('↑↑↑↑↑↑↑↑↑')
            
        while curr > k:
            curr -= nums[left]
            left += 1
            if curr < 8:
                print(nums[left:right+1])
            elif curr == 8:
                print('↓↓↓↓↓↓↓↓↓')
                print(nums[left:right+1])
                print('↑↑↑↑↑↑↑↑↑')
            

        answer = max(answer, (right-left+1))

    return answer


def main():
    nums = np.array([3, 1, 2, 7, 4, 2, 1, 1, 5])
    k = 8
    print(longSubArrSum(nums, k))

if __name__ == '__main__':
    main()
