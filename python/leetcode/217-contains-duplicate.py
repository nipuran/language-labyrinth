# Given an integer array nums, return true if any value appears at least twice in the array, and return
# false if every element is distinct.

# Example 1:
# input: nums = [1,2,3,1]
# output: true
# 
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# 
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def solutionOne(nums: list[int]) -> bool:
	count = {}
	for i, num in enumerate(nums):
		if num not in count:
			count[num] = 1
		else:
			return True
	return False 

def solutionTwo(nums: list[int]) -> bool:
	return len(set(nums)) < len(nums)

def main():
	example1 = [1,2,3,1]
	example2 = [1,2,3,4]
	example3 = [1,1,1,3,3,4,3,2,4,2]
	example4 = [3,1]

	print('Solution 1:')
	print(f'Example 1: {solutionOne(example1)}')
	print(f'Example 2: {solutionOne(example2)}')
	print(f'Example 3: {solutionOne(example3)}')

	print('Solution 2:')
	print(f'Example 1: {solutionTwo(example1)}')
	print(f'Example 2: {solutionTwo(example2)}')
	print(f'Example 3: {solutionTwo(example3)}')

if __name__ == "__main__":
    main()
