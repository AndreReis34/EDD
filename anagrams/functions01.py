def getHash(s):
	hashlist = []
	freq = [0]*26

	for ch in s:
		freq[ord(ch) - ord('a')] += 1

	for i in range(26):
		hashlist.append(str(freq[i]))
		hashlist.append("$")

	return ''.join(hashlist)


def anagrams(arr):
	res = []
	mp = {}

	for i in range(len(arr)):
		key = getHash(arr[i])

		if key not in mp:
			mp[key] = len(res)
			res.append([])


		res[mp[key]].append(arr[i])

	return res

def main():
	arr1 = ["act", "god", "cat", "dog", "tac"]
	arr2 = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
	print(anagrams(arr2))

