def isCyclicUtil(adj, u, visited, recStrack):
	if recStrack[u]:
		return True

	if visited[u]:
		return False

	visited[u] = True
	recStrack[u] = True

	for v in adj[u]:
		if isCyclicUtil(adj, v, visited, recStrack):
			return True

	recStrack[u] = False
	return False


def isCycle_directed(adj):
	V = len(adj)
	visited = [False]*V
	recStrack = [False]*V 

	for i in range(V):
		if not visited[i] and isCyclicUtil(adj, i, visited, recStrack):
			return True

	return False



