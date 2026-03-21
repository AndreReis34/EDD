def maximum_subarray_sum(arr):
	n = 0
	m = 1
	maximum = min(arr)

	while n != m:
		soma = 0
		for i in range(n, m):
			soma += arr[i]

		if soma > maximum:
			maximum = soma

		if m < len(arr):
			m+=1
		else:
			n+=1

	return maximum

