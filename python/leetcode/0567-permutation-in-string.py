def checkInclusion(s1: str, s2: str) -> bool:
	n1 = len(s1)
	n2 = len(s2)
	count_s1 = [0] * 26
	count_s2 = [0] * 26
	for i in range(n1):
		count_s1[ord(s1[i])-ord('a')] += 1
		count_s2[ord(s2[i])-ord('a')] += 1
	if count_s1 == count_s2: return True
	for i in range(n1, n2):
		count_s2[ord(s2[i])-ord('a')] += 1
		count_s2[ord(s2[i-n1])-ord('a')] -=1
		if count_s1 == count_s2: return True
	return False

testcases = []
testcases.append(checkInclusion("ab", "eidbaooo"))
testcases.append(checkInclusion("ab", "aidboaoo"))
testcases.append(checkInclusion("hello", "ooolleoooleh"))
testcases.append(checkInclusion("adc", "dcda"))
expected = [True, False, False, True]
for i in range(len(testcases)):
	if testcases[i] == expected[i]: print("passed")
