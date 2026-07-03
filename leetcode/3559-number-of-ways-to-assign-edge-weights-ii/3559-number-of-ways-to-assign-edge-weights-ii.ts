function assignEdgeWeights(
    edges: number[][],
    queries: number[][]
): number[] {

    const MOD = 1_000_000_007;

    // Used n to store number of nodes.
    const n = edges.length + 1;

    // Used graph as adjacency list.
    const graph: number[][] =
        Array.from(
            { length: n + 1 },
            () => []
        );

    // Built the tree.
    for (const [u, v] of edges) {

        graph[u].push(v);
        graph[v].push(u);
    }

    // Used LOG for binary lifting levels.
    const LOG = 18;

    // Used depth to store node depths.
    const depth =
        new Array<number>(n + 1).fill(0);

    // Used up for binary lifting ancestors.
    const up: number[][] =
        Array.from(
            { length: LOG },
            () => new Array<number>(n + 1).fill(0)
        );

    // Used queue for BFS traversal.
    const queue: number[] = [1];

    // Used visited to avoid revisiting nodes.
    const visited =
        new Array<boolean>(n + 1).fill(false);

    visited[1] = true;

    let head = 0;

    // Built depths and immediate parents.
    while (head < queue.length) {

        const node = queue[head++];

        for (const next of graph[node]) {

            if (visited[next]) {
                continue;
            }

            visited[next] = true;

            depth[next] = depth[node] + 1;

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

    // Precomputed powers of two modulo MOD.
    const pow2 =
        new Array<number>(n + 1).fill(1);

    for (let i = 1; i <= n; i++) {

        pow2[i] =
            Number(
                (BigInt(pow2[i - 1]) * 2n)
                % BigInt(MOD)
            );
    }

    // Used LCA to find lowest common ancestor.
    function lca(
        a: number,
        b: number
    ): number {

        // Lift deeper node to same depth.
        if (depth[a] < depth[b]) {
            [a, b] = [b, a];
        }

        let diff =
            depth[a] - depth[b];

        for (let k = 0; k < LOG; k++) {

            if (diff & (1 << k)) {

                a = up[k][a];
            }
        }

        // Found LCA immediately.
        if (a === b) {
            return a;
        }

        // Lift both nodes together.
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

        // Returned parent of both nodes.
        return up[0][a];
    }

    // Used answer to store results.
    const answer: number[] = [];

    // Processed all queries.
    for (const [u, v] of queries) {

        const ancestor =
            lca(u, v);

        // Calculated distance between nodes.
        const dist =
            depth[u]
            + depth[v]
            - 2 * depth[ancestor];

        // Empty path has no valid assignments.
        if (dist === 0) {

            answer.push(0);
        } else {

            // Answer equals 2^(distance - 1).
            answer.push(
                pow2[dist - 1]
            );
        }
    }

    // Returned all query answers.
    return answer;
}