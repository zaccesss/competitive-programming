class Solution {

    private let MOD = 1_000_000_007
    private let LOG = 18

    func assignEdgeWeights(
        _ edges: [[Int]],
        _ queries: [[Int]]
    ) -> [Int] {

        let n = edges.count + 1

        // Used adjacency list for the tree.
        var graph = Array(
            repeating: [Int](),
            count: n + 1
        )

        for edge in edges {

            let u = edge[0]
            let v = edge[1]

            graph[u].append(v)
            graph[v].append(u)
        }

        // Used depth to store node depths.
        var depth = Array(
            repeating: 0,
            count: n + 1
        )

        // Used binary lifting table.
        var up = Array(
            repeating: Array(
                repeating: 0,
                count: n + 1
            ),
            count: LOG
        )

        // Built depths and parents with BFS.
        var queue = [1]

        var visited = Array(
            repeating: false,
            count: n + 1
        )

        visited[1] = true

        var head = 0

        while head < queue.count {

            let node = queue[head]
            head += 1

            for next in graph[node] {

                if visited[next] {
                    continue
                }

                visited[next] = true

                depth[next] =
                    depth[node] + 1

                up[0][next] = node

                queue.append(next)
            }
        }

        // Built binary lifting table.
        for k in 1..<LOG {

            for node in 1...n {

                up[k][node] =
                    up[k - 1][
                        up[k - 1][node]
                    ]
            }
        }

        // Precomputed powers of 2 modulo MOD.
        var pow2 = Array(
            repeating: 1,
            count: n + 1
        )

        for i in 1...n {

            pow2[i] =
                Int(
                    (Int64(pow2[i - 1]) * 2)
                    % Int64(MOD)
                )
        }

        // Used LCA to find lowest common ancestor.
        func lca(
            _ startA: Int,
            _ startB: Int
        ) -> Int {

            var a = startA
            var b = startB

            if depth[a] < depth[b] {
                swap(&a, &b)
            }

            let diff =
                depth[a] - depth[b]

            for k in 0..<LOG {

                if (diff & (1 << k)) != 0 {

                    a = up[k][a]
                }
            }

            if a == b {
                return a
            }

            for k in stride(
                from: LOG - 1,
                through: 0,
                by: -1
            ) {

                if up[k][a] != up[k][b] {

                    a = up[k][a]
                    b = up[k][b]
                }
            }

            return up[0][a]
        }

        // Processed all queries.
        var answer = [Int]()

        answer.reserveCapacity(
            queries.count
        )

        for query in queries {

            let u = query[0]
            let v = query[1]

            let ancestor =
                lca(u, v)

            let dist =
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]

            if dist == 0 {

                answer.append(0)
            } else {

                answer.append(
                    pow2[dist - 1]
                )
            }
        }

        return answer
    }
}