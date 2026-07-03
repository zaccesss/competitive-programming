class Solution {
  List<int> assignEdgeWeights(
    List<List<int>> edges,
    List<List<int>> queries,
  ) {
    const int mod = 1000000007;
    const int log = 18;

    // Used n to store number of nodes.
    int n = edges.length + 1;

    // Used graph as adjacency list.
    List<List<int>> graph =
        List.generate(n + 1, (_) => []);

    // Built the tree.
    for (var edge in edges) {
      int u = edge[0];
      int v = edge[1];

      graph[u].add(v);
      graph[v].add(u);
    }

    // Used depth to store node depths.
    List<int> depth =
        List.filled(n + 1, 0);

    // Used up for binary lifting ancestors.
    List<List<int>> up =
        List.generate(
          log,
          (_) => List.filled(n + 1, 0),
        );

    // Used queue for BFS traversal.
    List<int> queue = [1];

    List<bool> visited =
        List.filled(n + 1, false);

    visited[1] = true;

    int head = 0;

    // Built depths and immediate parents.
    while (head < queue.length) {
      int node = queue[head++];

      for (int next in graph[node]) {
        if (visited[next]) {
          continue;
        }

        visited[next] = true;

        depth[next] = depth[node] + 1;

        up[0][next] = node;

        queue.add(next);
      }
    }

    // Built binary lifting table.
    for (int k = 1; k < log; k++) {
      for (int node = 1; node <= n; node++) {
        up[k][node] =
            up[k - 1][
                up[k - 1][node]
            ];
      }
    }

    // Precomputed powers of two modulo mod.
    List<int> pow2 =
        List.filled(n + 1, 1);

    for (int i = 1; i <= n; i++) {
      pow2[i] =
          (pow2[i - 1] * 2) % mod;
    }

    // Used LCA to find lowest common ancestor.
    int lca(int a, int b) {
      if (depth[a] < depth[b]) {
        int temp = a;
        a = b;
        b = temp;
      }

      int diff = depth[a] - depth[b];

      for (int k = 0; k < log; k++) {
        if ((diff & (1 << k)) != 0) {
          a = up[k][a];
        }
      }

      if (a == b) {
        return a;
      }

      for (int k = log - 1; k >= 0; k--) {
        if (up[k][a] != up[k][b]) {
          a = up[k][a];
          b = up[k][b];
        }
      }

      return up[0][a];
    }

    // Used answer to store results.
    List<int> answer = [];

    // Processed all queries.
    for (var query in queries) {
      int u = query[0];
      int v = query[1];

      int ancestor = lca(u, v);

      // Calculated distance between nodes.
      int dist =
          depth[u] +
          depth[v] -
          2 * depth[ancestor];

      if (dist == 0) {
        answer.add(0);
      } else {
        // Answer equals 2^(distance - 1).
        answer.add(
          pow2[dist - 1],
        );
      }
    }

    // Returned all query answers.
    return answer;
  }
}