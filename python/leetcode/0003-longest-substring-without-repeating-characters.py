def lengthOfLongestSubstring(s):
	l = 0
	r = 1
	count = 0
	if len(s) == 1:
		count += 1
		return count
	while r < len(s):
		if s[r] in s[l:r]:
			count = max(count, len(s[l:r]))
			l += 1
		else:
			r += 1
			count = max(count, len(s[l:r]))
	return count

case_1 = lengthOfLongestSubstring("abcabcbb")
print(case_1)
case_2 = lengthOfLongestSubstring("bbbbb")
print(case_2)
case_3 = lengthOfLongestSubstring("pwwkew")
print(case_3)
case_4 = lengthOfLongestSubstring(" ")
print(case_4)
case_5 = lengthOfLongestSubstring("au")
print(case_5)
