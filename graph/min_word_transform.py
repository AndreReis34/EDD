def minWordTranform(start, target, mp):
	if start == target:
		return 1

	mini = float('inf')

	mp[start] = 1

	for i in range(len(start)):
		original_char = start[i]

		for ch in 'abcdefghijklmnopqrstuvwxyz':
			new_word = start[:i] + ch +start[i+1:]

			if new_word in mp and mp[new_word] == 0:
				mini  = min(mini, 1+minWordTranform(new_word, target, mp))

	mp[start] = 0
	return mini

def wordLadder(start, target, arr):
	mp = {word: 0 for word in arr}
	print(mp)

	result = minWordTranform(start, target, mp)
	if(result == float('inf')):
		result = 0

	return result

from collections import deque

def wordLadder01(start, target, arr):
	if(start == target):
		return 0

	st = set(arr)

	res = 0
	m = len(start)


	words = deque()
	words.append(start)

	while words:
		res+=1
		length = len(words)

		for _ in range(length):
			word = words.popleft()

			for i in range(m):
				ch = word[i]

				for letter in range(ord('a'), ord('z')+1):
					word = word[:i]+chr(letter)+word[i+1:]

					if word not in st:
						continue
					if word == target:
						return res+1

					st.remove(word)

					words.append(word)

				word = word[:i]+ch+word[i+1:]

	return 0 

