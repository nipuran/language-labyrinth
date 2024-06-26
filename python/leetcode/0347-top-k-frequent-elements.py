# Given an ineger array nums and an integer k, return the k most
# frequent elements. You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from collections import defaultdict

def topKFrequent(nums: list[int], k: int):
	count = dict()
	freq = [[] for i in range(len(nums) + 1)]
	
	# d for 'duplicate'. e for 'exist'

	for i, num in enumerate(nums):
		if num in count:
			count[num] += 1
		else:
			count[num] = 1
	
	for i, j in count.items():
		freq[j].append(i)
	
	res = list()
	for i in range(len(freq) -1, 0, -1):
		for j in freq[i]:
			res.append(j)
			if len(res) == k:
				return res

def main():
	print(topKFrequent([1,1,1,2,2,3], 2))

if __name__ == "__main__":
	main()
