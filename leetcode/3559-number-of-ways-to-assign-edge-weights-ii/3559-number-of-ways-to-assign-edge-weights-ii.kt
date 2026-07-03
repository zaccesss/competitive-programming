class Solution {

    companion object {
        private const val MOD = 1_000_000_007L
        private const val LOG = 18
    }

    fun assignEdgeWeights(
        edges: Array<IntArray>,
        queries: Array<IntArray>
    ): IntArray {

        val n = edges.size + 1

        // Used adjacency list for the tree.
        val graph = Array(n + 1) {
            mutableListOf<Int>()
        }

        for (edge in edges) {

            val u = edge[0]
            val v = edge[1]

            graph[u].add(v)
            graph[v].add(u)
        }

        // Used depth to store node depths.
        val depth = IntArray(n + 1)

        // Used binary lifting table.
        val up = Array(LOG) {
            IntArray(n + 1)
        }

        // Built depths and parents with BFS.
        val queue = ArrayDeque<Int>()

        val visited = BooleanArray(n + 1)

        queue.addLast(1)
        visited[1] = true

        while (queue.isNotEmpty()) {

            val node = queue.removeFirst()

            for (next in graph[node]) {

                if (visited[next]) {
                    continue
                }

                visited[next] = true

                depth[next] = depth[node] + 1

                up[0][next] = node

                queue.addLast(next)
            }
        }

        // Built binary lifting table.
        for (k in 1 until LOG) {

            for (node in 1..n) {

                up[k][node] =
                    up[k - 1][
                        up[k - 1][node]
                    ]
            }
        }

        // Precomputed powers of 2 modulo MOD.
        val pow2 = IntArray(n + 1)

        pow2[0] = 1

        for (i in 1..n) {

            pow2[i] =
                ((pow2[i - 1].toLong() * 2) % MOD)
                    .toInt()
        }

        // Used LCA to find lowest common ancestor.
        fun lca(
            startA: Int,
            startB: Int
        ): Int {

            var a = startA
            var b = startB

            if (depth[a] < depth[b]) {
                val temp = a
                a = b
                b = temp
            }

            val diff = depth[a] - depth[b]

            for (k in 0 until LOG) {

                if ((diff and (1 shl k)) != 0) {

                    a = up[k][a]
                }
            }

            if (a == b) {
                return a
            }

            for (k in LOG - 1 downTo 0) {

                if (up[k][a] != up[k][b]) {

                    a = up[k][a]
                    b = up[k][b]
                }
            }

            return up[0][a]
        }

        // Processed all queries.
        val answer = IntArray(queries.size)

        for (i in queries.indices) {

            val u = queries[i][0]
            val v = queries[i][1]

            val ancestor = lca(u, v)

            val dist =
                depth[u] +
                depth[v] -
                2 * depth[ancestor]

            answer[i] =
                if (dist == 0) {
                    0
                } else {
                    pow2[dist - 1]
                }
        }

        return answer
    }
}