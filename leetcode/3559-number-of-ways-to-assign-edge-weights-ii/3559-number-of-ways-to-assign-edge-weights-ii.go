func assignEdgeWeights(edges [][]int, queries [][]int) []int {

	const MOD = 1000000007
	const LOG = 18

	n := len(edges) + 1

	// Used adjacency list for the tree.
	graph := make([][]int, n+1)

	for _, edge := range edges {
		u := edge[0]
		v := edge[1]

		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	// Used depth to store node depths.
	depth := make([]int, n+1)

	// Used binary lifting table.
	up := make([][]int, LOG)

	for i := 0; i < LOG; i++ {
		up[i] = make([]int, n+1)
	}

	// Built depths and parents with BFS.
	queue := []int{1}

	visited := make([]bool, n+1)
	visited[1] = true

	for head := 0; head < len(queue); head++ {

		node := queue[head]

		for _, next := range graph[node] {

			if visited[next] {
				continue
			}

			visited[next] = true

			depth[next] = depth[node] + 1

			up[0][next] = node

			queue = append(queue, next)
		}
	}

	// Built binary lifting table.
	for k := 1; k < LOG; k++ {
		for node := 1; node <= n; node++ {
			up[k][node] = up[k-1][up[k-1][node]]
		}
	}

	// Precomputed powers of 2 modulo MOD.
	pow2 := make([]int, n+1)

	pow2[0] = 1

	for i := 1; i <= n; i++ {
		pow2[i] = int((2 * int64(pow2[i-1])) % MOD)
	}

	// Used LCA to find lowest common ancestor.
	var lca func(int, int) int

	lca = func(a, b int) int {

		if depth[a] < depth[b] {
			a, b = b, a
		}

		diff := depth[a] - depth[b]

		for k := 0; k < LOG; k++ {
			if diff&(1<<k) != 0 {
				a = up[k][a]
			}
		}

		if a == b {
			return a
		}

		for k := LOG - 1; k >= 0; k-- {
			if up[k][a] != up[k][b] {
				a = up[k][a]
				b = up[k][b]
			}
		}

		return up[0][a]
	}

	// Processed all queries.
	answer := make([]int, len(queries))

	for i, query := range queries {

		u := query[0]
		v := query[1]

		ancestor := lca(u, v)

		dist := depth[u] + depth[v] - 2*depth[ancestor]

		if dist == 0 {
			answer[i] = 0
		} else {
			answer[i] = pow2[dist-1]
		}
	}

	return answer
}