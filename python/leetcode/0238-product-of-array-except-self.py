# Given an ineger array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums except
# nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in 0(n) time and without using
# the division operation.

# def productExceptSelf(nums):
# 	answer = [1 for i in range(len(nums))]
# 	o = 0 # pointer for output
# 	i = 0 # pointer for input
# 
# 	while o != len(nums):
# 		if i == o:
# 			i += 1
# 		else:
# 			answer[o] *= nums[i]
# 			i += 1
# 
# 		if i == len(nums):
# 			i = 0
# 			o += 1
# 	return answer

def productExceptSelf(nums):
	answer = [1 for i in nums]
	prefix = postfix = 1
	for i in range(len(nums)-1):
		prefix *= nums[i]
		answer[i+1] = prefix
	for i in range(len(nums)-1, 0, -1):
		postfix *= nums[i]
		answer[i-1] *= postfix
	return answer

def main():
	nums = [1, 2, 2, 4]
	print(productExceptSelf(nums))

if __name__ == "__main__":
	main()
