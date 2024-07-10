def characterReplacement(s: str, k: int) -> int:
	l = 0
	r = 0
	count = {}
	res = 0
	while r < len(s):
		if s[r] in count:
			count[s[r]] += 1
		else:
			count[s[r]] = 1
		maxf = max(count.values())
		if (r-l+1) - maxf > k:
			count[s[l]] -= 1
			l += 1
		res = max(res, (r-l+1))
		r += 1
	return res

case_1 = characterReplacement("ABAB", 2)
print(case_1)
case_2 = characterReplacement("AABABBA", 1)
print(case_2)
case_3 = characterReplacement("AAAA", 0)
print(case_3)
