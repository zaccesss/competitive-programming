function assignEdgeWeights(
    edges: number[][],
    queries: number[][]
): number[] {

    const MOD = 1_000_000_007;

    // used n to store number of nodes.
    const n = edges.length + 1;

    // used graph as adjacency list.
    const graph: number[][] =
        Array.from(
            { length: n + 1 },
            () => []
        );

    // built the tree.
    for (const [u, v] of edges) {

        graph[u].push(v);
        graph[v].push(u);
    }

    // used LOG for binary lifting levels.
    const LOG = 18;

    // used depth to store node depths.
    const depth =
        new Array<number>(n + 1).fill(0);

    // used up for binary lifting ancestors.
    const up: number[][] =
        Array.from(
            { length: LOG },
            () => new Array<number>(n + 1).fill(0)
        );

    // used queue for BFS traversal.
    const queue: number[] = [1];

    // used visited to avoid revisiting nodes.
    const visited =
        new Array<boolean>(n + 1).fill(false);

    visited[1] = true;

    let head = 0;

    // built depths and immediate parents.
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

    // built binary lifting table.
    for (let k = 1; k < LOG; k++) {

        for (let node = 1; node <= n; node++) {

            up[k][node] =
                up[k - 1][
                    up[k - 1][node]
                ];
        }
    }

    // precomputed powers of two modulo MOD.
    const pow2 =
        new Array<number>(n + 1).fill(1);

    for (let i = 1; i <= n; i++) {

        pow2[i] =
            Number(
                (BigInt(pow2[i - 1]) * 2n)
                % BigInt(MOD)
            );
    }

    // used LCA to find lowest common ancestor.
    function lca(
        a: number,
        b: number
    ): number {

        // lift deeper node to same depth.
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

        // found LCA immediately.
        if (a === b) {
            return a;
        }

        // lift both nodes together.
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

        // returned parent of both nodes.
        return up[0][a];
    }

    // used answer to store results.
    const answer: number[] = [];

    // processed all queries.
    for (const [u, v] of queries) {

        const ancestor =
            lca(u, v);

        // calculated distance between nodes.
        const dist =
            depth[u]
            + depth[v]
            - 2 * depth[ancestor];

        // empty path has no valid assignments.
        if (dist === 0) {

            answer.push(0);
        } else {

            // answer equals 2^(distance - 1).
            answer.push(
                pow2[dist - 1]
            );
        }
    }

    // returned all query answers.
    return answer;
}