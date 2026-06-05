def addEdge(adj, u,v):
		adj[u].append(v)
		adj[v].append(u)

def isSafe(i, j, n, m):
	return 0 <= i < n and 0 <= j < m

def isSafe01(grid, r, c, visited):
	n = len(grid)
	m = len(grid[0])

	return (0 <= r < n and 0 <= c < m and grid[r][c] == "L"
		and not visited[r][c])
	
