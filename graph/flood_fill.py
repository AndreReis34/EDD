def dfs(img, x, y, oldColor, newColor):
	if(x < 0 or x >= len(img) or y < 0 or x >= len(img[0])
		or img[x][y] != oldColor):
		return

	img[x][y] = newColor

	dfs(img, x+1, y, oldColor, newColor)
	dfs(img, x-1, y, oldColor, newColor)
	dfs(img, x, y+1, oldColor, newColor)
	dfs(img, x, y-1, oldColor, newColor)


def floodFill(img, sr, sc, newColor):
	if img[sr][sc] == newColor:
		return img

	oldColor = img[sr][sc]
	dfs(img, sr, sc, oldColor, newColor)

	return img
