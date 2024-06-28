
def minWindow(s: str, t: str) -> str:
	if t == "": return ""
	countT, window = {}, {}
	for c in t:
		if c in countT:
			countT[c] += 1
		else:
			countT[c] = 1
	res, reslen = [-1, -1], float("inf")
	have, need = 0, len(countT)
	l = 0
	for r in range(len(s)):
		c = s[r]
		if c in window:
			window[c] += 1
		else:
			window[c] = 1

		if c in countT and window[c] == countT[c]:
			have += 1

		while have == need:
			if (r-l+1) < reslen:
				reslen = r-l+1
				res = [l, r]

			window[s[l]] -= 1

			if s[l] in countT and window[s[l]] < countT[s[l]]:
				have -= 1
			l += 1

	l, r = res
	return s[l:r+1] if reslen != float("inf") else ""

case_1 = minWindow("ADOECODEBANC", "ABC")
print(case_1)
case_2 = minWindow("a", "a")
print(case_2)
case_3 = minWindow("a", "aa")
print(case_3)
