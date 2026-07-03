# @param {Integer[][]} edges
# @param {Integer[][]} queries
# @return {Integer[]}
def assign_edge_weights(edges, queries)

    mod = 1_000_000_007
    log = 18

    n = edges.length + 1

    # Used adjacency list for the tree.
    graph = Array.new(n + 1) { [] }

    edges.each do |u, v|

        graph[u] << v
        graph[v] << u
    end

    # Used depth to store node depths.
    depth = Array.new(n + 1, 0)

    # Used binary lifting table.
    up = Array.new(log) do
        Array.new(n + 1, 0)
    end

    # Built depths and parents with BFS.
    queue = [1]

    visited = Array.new(n + 1, false)

    visited[1] = true

    head = 0

    while head < queue.length

        node = queue[head]

        head += 1

        graph[node].each do |nxt|

            next if visited[nxt]

            visited[nxt] = true

            depth[nxt] =
                depth[node] + 1

            up[0][nxt] = node

            queue << nxt
        end
    end

    # Built binary lifting table.
    (1...log).each do |k|

        (1..n).each do |node|

            up[k][node] =
                up[k - 1][
                    up[k - 1][node]
                ]
        end
    end

    # Precomputed powers of 2 modulo mod.
    pow2 = Array.new(n + 1, 1)

    (1..n).each do |i|

        pow2[i] =
            (pow2[i - 1] * 2) % mod
    end

    # Used LCA to find lowest common ancestor.
    lca = lambda do |a, b|

        if depth[a] < depth[b]
            a, b = b, a
        end

        diff = depth[a] - depth[b]

        (0...log).each do |k|

            if (diff & (1 << k)) != 0

                a = up[k][a]
            end
        end

        return a if a == b

        (log - 1).downto(0) do |k|

            if up[k][a] != up[k][b]

                a = up[k][a]
                b = up[k][b]
            end
        end

        up[0][a]
    end

    # Processed all queries.
    answer = []

    queries.each do |u, v|

        ancestor = lca.call(u, v)

        dist =
            depth[u] +
            depth[v] -
            2 * depth[ancestor]

        if dist == 0

            answer << 0
        else

            answer << pow2[dist - 1]
        end
    end

    answer
end