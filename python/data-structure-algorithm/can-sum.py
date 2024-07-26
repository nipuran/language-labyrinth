from typing import List

def canSum(targetSum: int, nums: List[int], memo=None) -> bool:
    if (memo is None): memo = {}
    if (targetSum in memo): return memo[targetSum]
    if (targetSum == 0): return True
    if (targetSum < 0): return False

    for n in nums:
        remainder: int = targetSum - n
        if (canSum(remainder, nums, memo) == True):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(40, [4, 3, 21, 43, 10]))
print(canSum(10, [5, 2]))
print(canSum(7, [2, 4]))
print(canSum(300, [7, 14]))
