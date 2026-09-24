class Solution {

    private static final int MOD = 1_000_000_007;
    private static final int LOG = 18;

    public int[] assignEdgeWeights(
        int[][] edges,
        int[][] queries
    ) {

        // used n to store number of nodes.
        int n = edges.length + 1;

        // built adjacency list for the tree.
        List<Integer>[] graph =
            new ArrayList[n + 1];

        for (int i = 0; i <= n; i++) {

            graph[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {

            int u = edge[0];
            int v = edge[1];

            graph[u].add(v);
            graph[v].add(u);
        }

        // used depth to store node depths.
        int[] depth = new int[n + 1];

        // used up for binary lifting ancestors.
        int[][] up =
            new int[LOG][n + 1];

        // built depths and immediate parents using BFS.
        boolean[] visited =
            new boolean[n + 1];

        Queue<Integer> queue =
            new ArrayDeque<>();

        queue.offer(1);

        visited[1] = true;

        while (!queue.isEmpty()) {

            int node = queue.poll();

            for (int next : graph[node]) {

                if (visited[next]) {
                    continue;
                }

                visited[next] = true;

                depth[next] =
                    depth[node] + 1;

                up[0][next] = node;

                queue.offer(next);
            }
        }

        // built binary lifting table.
        for (int k = 1; k < LOG; k++) {

            for (int node = 1; node <= n; node++) {

                up[k][node] =
                    up[k - 1][
                        up[k - 1][node]
                    ];
            }
        }

        // precomputed powers of two modulo MOD.
        int[] pow2 =
            new int[n + 1];

        pow2[0] = 1;

        for (int i = 1; i <= n; i++) {

            pow2[i] =
                (int) (
                    (pow2[i - 1] * 2L)
                    % MOD
                );
        }

        // used answer to store results.
        int[] answer =
            new int[queries.length];

        // processed all queries.
        for (int i = 0; i < queries.length; i++) {

            int u = queries[i][0];
            int v = queries[i][1];

            // found lowest common ancestor.
            int ancestor =
                lca(
                    u,
                    v,
                    depth,
                    up
                );

            // calculated distance.
            int dist =
                depth[u]
                + depth[v]
                - 2 * depth[ancestor];

            // empty path has no valid assignments.
            if (dist == 0) {

                answer[i] = 0;
            } else {

                // answer equals 2^(distance - 1).
                answer[i] =
                    pow2[dist - 1];
            }
        }

        return answer;
    }

    // used binary lifting to find LCA.
    private int lca(
        int a,
        int b,
        int[] depth,
        int[][] up
    ) {

        if (depth[a] < depth[b]) {

            int temp = a;
            a = b;
            b = temp;
        }

        int diff =
            depth[a] - depth[b];

        // lifted deeper node.
        for (int k = 0; k < LOG; k++) {

            if (
                (diff & (1 << k))
                != 0
            ) {

                a = up[k][a];
            }
        }

        // found LCA immediately.
        if (a == b) {

            return a;
        }

        // lifted both nodes together.
        for (
            int k = LOG - 1;
            k >= 0;
            k--
        ) {

            if (
                up[k][a]
                != up[k][b]
            ) {

                a = up[k][a];
                b = up[k][b];
            }
        }

        // returned lowest common ancestor.
        return up[0][a];
    }
}