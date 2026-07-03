class Solution {
public:
    static constexpr long long MOD = 1'000'000'007;

    vector<int> assignEdgeWeights(
        vector<vector<int>>& edges,
        vector<vector<int>>& queries
    ) {
        int n = edges.size() + 1;

        vector<vector<int>> graph(n + 1);

        for (auto& e : edges) {
            int u = e[0];
            int v = e[1];

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int LOG = 18;

        vector<int> depth(n + 1, 0);

        vector<vector<int>> up(
            LOG,
            vector<int>(n + 1)
        );

        queue<int> q;
        q.push(1);

        vector<bool> visited(n + 1, false);
        visited[1] = true;

        while (!q.empty()) {

            int node = q.front();
            q.pop();

            for (int next : graph[node]) {

                if (visited[next]) {
                    continue;
                }

                visited[next] = true;

                depth[next] = depth[node] + 1;

                up[0][next] = node;

                q.push(next);
            }
        }

        for (int k = 1; k < LOG; k++) {

            for (int node = 1; node <= n; node++) {

                up[k][node] =
                    up[k - 1][
                        up[k - 1][node]
                    ];
            }
        }

        vector<int> pow2(n + 1, 1);

        for (int i = 1; i <= n; i++) {

            pow2[i] =
                (2LL * pow2[i - 1]) % MOD;
        }

        auto lca = [&](int a, int b) {

            if (depth[a] < depth[b]) {
                swap(a, b);
            }

            int diff = depth[a] - depth[b];

            for (int k = 0; k < LOG; k++) {

                if (diff & (1 << k)) {
                    a = up[k][a];
                }
            }

            if (a == b) {
                return a;
            }

            for (int k = LOG - 1; k >= 0; k--) {

                if (up[k][a] != up[k][b]) {

                    a = up[k][a];
                    b = up[k][b];
                }
            }

            return up[0][a];
        };

        vector<int> answer;
        answer.reserve(queries.size());

        for (auto& query : queries) {

            int u = query[0];
            int v = query[1];

            int ancestor = lca(u, v);

            int dist =
                depth[u]
                + depth[v]
                - 2 * depth[ancestor];

            if (dist == 0) {
                answer.push_back(0);
            } else {
                answer.push_back(
                    pow2[dist - 1]
                );
            }
        }

        return answer;
    }
};