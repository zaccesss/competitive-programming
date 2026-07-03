/**
 * @param {number[][]} edges
 * @param {number[][]} queries
 * @return {number[]}
 */
var assignEdgeWeights = function(edges, queries) {

    const MOD = 1000000007;
    const LOG = 18;

    const n = edges.length + 1;

    // Used adjacency list for the tree.
    const graph =
        Array.from(
            { length: n + 1 },
            () => []
        );

    for (const [u, v] of edges) {

        graph[u].push(v);
        graph[v].push(u);
    }

    // Used depth to store node depths.
    const depth =
        new Array(n + 1).fill(0);

    // Used binary lifting table.
    const up =
        Array.from(
            { length: LOG },
            () => new Array(n + 1).fill(0)
        );

    // Built depths and parents with BFS.
    const queue = [1];

    const visited =
        new Array(n + 1).fill(false);

    visited[1] = true;

    let head = 0;

    while (head < queue.length) {

        const node = queue[head++];

        for (const next of graph[node]) {

            if (visited[next]) {
                continue;
            }

            visited[next] = true;

            depth[next] =
                depth[node] + 1;

            up[0][next] = node;

            queue.push(next);
        }
    }

    // Built binary lifting table.
    for (let k = 1; k < LOG; k++) {

        for (let node = 1; node <= n; node++) {

            up[k][node] =
                up[k - 1][
                    up[k - 1][node]
                ];
        }
    }

    // Precomputed powers of 2 modulo MOD.
    const pow2 =
        new Array(n + 1).fill(1);

    for (let i = 1; i <= n; i++) {

        pow2[i] =
            (pow2[i - 1] * 2) % MOD;
    }

    // Used LCA to find lowest common ancestor.
    function lca(a, b) {

        if (depth[a] < depth[b]) {
            [a, b] = [b, a];
        }

        const diff =
            depth[a] - depth[b];

        for (let k = 0; k < LOG; k++) {

            if (diff & (1 << k)) {

                a = up[k][a];
            }
        }

        if (a === b) {
            return a;
        }

        for (
            let k = LOG - 1;
            k >= 0;
            k--
        ) {

            if (
                up[k][a] !== up[k][b]
            ) {

                a = up[k][a];
                b = up[k][b];
            }
        }

        return up[0][a];
    }

    // Processed all queries.
    const answer = [];

    for (const [u, v] of queries) {

        const ancestor =
            lca(u, v);

        const dist =
            depth[u]
            + depth[v]
            - 2 * depth[ancestor];

        if (dist === 0) {

            answer.push(0);
        } else {

            answer.push(
                pow2[dist - 1]
            );
        }
    }

    return answer;
};