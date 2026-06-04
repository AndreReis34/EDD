def addEdge(adj, u,v):
		adj[u].append(v)
		adj[v].append(u)

def isSafe(i, j, n, m):
	return 0 <= i < n and 0 <= j < m

