from functions import isSafe01

def dfs(grid, r, c, visited):
	visited[r][c] = True

	dr = [-1,-1,-1,0,0,1,1,1]
	dc = [-1,0,1,-1,1,-1,0,1]

	for k in range(8):
		nr = r + dr[k]
		nc = c + dc[k]

		if isSafe01(grid, nr, nc, visited):
			dfs(grid, nr, nc, visited)

def countIslands(grid):
	n = len(grid)
	m = len(grid[0])

	visited = [[False for _ in range(m)] for _ in range(n)]

	islands = 0

	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'L' and not visited[i][j]:
				dfs(grid, i, j, visited)
				islands += 1
	print(visited)
	return islands

#################################################################
#################################################################

class DisjointSet:
	def __init__(self, n):
		self.parent = list(range(n))
		self.rank = [0]*n

	def find(self,x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def unite(self,x,y):
		xRoot = self.find(x)
		yRoot = self.find(y)

		if xRoot == yRoot:
			return 
		
		if self.rank[xRoot] < self.rank[yRoot]:
			self.parent[xRoot] = yRoot
		elif self.rank[yRoot] < self.rank[xRoot]:
			self.parent[yRoot] = xRoot
		else:
			self.parent[yRoot] = xRoot
			self.rank[xRoot] += 1

def countIslands01(grid):
    n = len(grid)
    m = len(grid[0])

    ds = DisjointSet(n*m)

    directions = [
        (-1, 0), (1,0), (0,-1), (0,1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'L':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'L':
                        ds.unite(r*m+c, nr*m+nc)

    uniqueIslands = set()
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'L':
                uniqueIslands.add(ds.find(r*m+c))

    return len(uniqueIslands)

