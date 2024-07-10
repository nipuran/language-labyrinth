from sys import argv 

n = len(argv)

print(f"Total number of arguments: {n}")

name = argv[0]
print(f"The name of the file: {name}")

print("Arguments passed:", end=" ")
for i in range(1, n):
	print(argv[i], end=" ")

print()
