# Design an algorithm to encode a list of strings to a string. The encoded string is 
# then sent over the network and is decoded back to the original list of strings.
# Please implement encode and decode
#
# Example
# Example 1
# Input: ["lint", "code", "love", "you"]
# Output: ["lint", "code", "love", "you"]
# Explaination:
# One possible encode method is: "lint:;code:;love:;you"

def encode(strs: list[str]) -> str:
	res = ''
	for s in strs:
		res += str(len(s)) + '#' + s
	return res

def decode(string: str) -> list[str]:
	res = []
	i = 0
	while i < len(string):
		j = i
		while string[j] != '#':
			j += 1
		length = int(string[i:j])
		res.append(string[j+1: j+1 + length])
		i = j+1 + length
	return res
		

def main():
	strs = ["lint", "code", "love", "you"]
	en = encode(strs)
	print(en)
	de = decode(en)
	print(de)

if __name__ == "__main__":
	main()
