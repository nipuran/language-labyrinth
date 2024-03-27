# 49. Group Anagrams

# Give an array of strings strs, group the anagrams together. you 
# can return the answer in any order.

# An Angram is a word or phrase formed by rearranging the letter of
# a different word or phrase, typically using all the original letter exactly
# once.


# Example 1:
# Input: strs =
# ["eat", "tea","tan", "ate", "nat", "bat"]
# Output: [["bat"], ["hat", "tan"],
# ["ate", "eat", "tea"]]

from collections import defaultdict

def func(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26 # a ... z
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return res.values()

def main():
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(func(strs))

if __name__ == "__main__":
	main()
