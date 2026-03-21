def longestUniqueSubstr(s):
	lenAtual = 0
	maxLen = 0
	subString = ""

	for i in range(0, len(s)-1):
		subString = subString+s[i]

		lenAtual = len(subString)


		if lenAtual > maxLen:
			maxLen = lenAtual

		if s[i+1] in subString:
			subString = ""
			continue



	return maxLen



