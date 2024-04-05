def binary_search(target, array):
	left = 0
	right = len(array)-1

	while left<=right:
		mid = (left+right)//2

		if array[mid] == target:
			return f'the index of the value: {mid}'
		elif array[mid] > target:
			right=mid-1 
		elif array[mid] < target:
			left=mid+1
		else:
			return 'Not Found'

def main():
	array = [2,3,4,5,6,7,8,9]
	print(binary_search(2, array))

if __name__ == '__main__':
	main()

