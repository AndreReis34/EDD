def search2D(grid, row, col, word):
	m = len(grid)
	n = len(grid[0])

	if grid[row][col] != word[0]:
		return False

	lenWord = len(word)

	x = [-1, -1, -1, 0, 0 , 1, 1, 1]
	y = [-1, 0, 1, -1, 1, -1, 0, 1]

	for dir in range(8):
		currX, currY = row+x[dir], col+y[dir]
		k = 1

		while k < lenWord:
			if currX >= m or currx < 0 or currY >= n or currY < 0:
				break

			if grid[currX][currY] != word[k]:
				break

			currX += x[dir]
			currY += y[dir]

			k+=1

		if k == lenWord:
			return True

	return False

def searchWord02(grid, word):
	m = len(grid)
	n = len(grid[0])

	ans = []

	for i in range(m):
		for j in range(n):
			if search2D(grid, i, j, word):
				ans.append([i, j])

	return ans

def  printResult02(ans):
	for coord in ans:
		print(f"{{{coord[0]}, {coord[1]}}}", end="")
	print()

