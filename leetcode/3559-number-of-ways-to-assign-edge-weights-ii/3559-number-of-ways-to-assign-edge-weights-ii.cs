public class Solution
{
    public int[] AssignEdgeWeights(int[][] edges, int[][] queries)
    {
        const long MOD = 1_000_000_007;

        int n = edges.Length + 1;

        // Used adjacency list for the tree.
        List<int>[] graph = new List<int>[n + 1];

        for (int i = 0; i <= n; i++)
        {
            graph[i] = new List<int>();
        }

        foreach (var edge in edges)
        {
            int u = edge[0];
            int v = edge[1];

            graph[u].Add(v);
            graph[v].Add(u);
        }

        int LOG = 18;

        // Used depth to store node depths.
        int[] depth = new int[n + 1];

        // Used binary lifting table.
        int[,] up = new int[LOG, n + 1];

        // Built depths and immediate parents.
        Queue<int> queue = new Queue<int>();

        bool[] visited = new bool[n + 1];

        queue.Enqueue(1);
        visited[1] = true;

        while (queue.Count > 0)
        {
            int node = queue.Dequeue();

            foreach (int next in graph[node])
            {
                if (visited[next])
                {
                    continue;
                }

                visited[next] = true;

                depth[next] = depth[node] + 1;

                up[0, next] = node;

                queue.Enqueue(next);
            }
        }

        // Built binary lifting ancestors.
        for (int k = 1; k < LOG; k++)
        {
            for (int node = 1; node <= n; node++)
            {
                up[k, node] =
                    up[k - 1, up[k - 1, node]];
            }
        }

        // Precomputed powers of two modulo MOD.
        int[] pow2 = new int[n + 1];

        pow2[0] = 1;

        for (int i = 1; i <= n; i++)
        {
            pow2[i] =
                (int)((2L * pow2[i - 1]) % MOD);
        }

        // Used LCA to find lowest common ancestor.
        int Lca(int a, int b)
        {
            if (depth[a] < depth[b])
            {
                (a, b) = (b, a);
            }

            int diff = depth[a] - depth[b];

            for (int k = 0; k < LOG; k++)
            {
                if ((diff & (1 << k)) != 0)
                {
                    a = up[k, a];
                }
            }

            if (a == b)
            {
                return a;
            }

            for (int k = LOG - 1; k >= 0; k--)
            {
                if (up[k, a] != up[k, b])
                {
                    a = up[k, a];
                    b = up[k, b];
                }
            }

            return up[0, a];
        }

        // Used answer to store query results.
        int[] answer = new int[queries.Length];

        for (int i = 0; i < queries.Length; i++)
        {
            int u = queries[i][0];
            int v = queries[i][1];

            int ancestor = Lca(u, v);

            int dist =
                depth[u]
                + depth[v]
                - 2 * depth[ancestor];

            // Added zero for empty paths.
            if (dist == 0)
            {
                answer[i] = 0;
            }
            else
            {
                answer[i] = pow2[dist - 1];
            }
        }

        // Returned all query answers.
        return answer;
    }
}