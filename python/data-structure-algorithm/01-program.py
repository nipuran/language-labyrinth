import numpy as np

nums = np.random.randint(1, 9, size=8)


def whichMax(nums):
    maxNum = 0
    for num in nums:
        if num > maxNum:
            maxNum = num
    return maxNum

print(nums)
print(whichMax(nums))
