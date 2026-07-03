object Solution {
    def assignEdgeWeights(
        edges: Array[Array[Int]],
        queries: Array[Array[Int]]
    ): Array[Int] = {

        val MOD = 1000000007
        val LOG = 18

        // Used n to store number of nodes.
        val n = edges.length + 1

        // Used graph as adjacency list.
        val graph =
            Array.fill(n + 1)(
                scala.collection.mutable.ArrayBuffer[Int]()
            )

        // Built the tree.
        for (edge <- edges) {

            val u = edge(0)
            val v = edge(1)

            graph(u) += v
            graph(v) += u
        }

        // Used depth to store node depths.
        val depth =
            Array.fill(n + 1)(0)

        // Used up for binary lifting ancestors.
        val up =
            Array.fill(LOG, n + 1)(0)

        // Used queue for BFS traversal.
        val queue =
            scala.collection.mutable.Queue[Int]()

        val visited =
            Array.fill(n + 1)(false)

        queue.enqueue(1)

        visited(1) = true

        // Built depths and immediate parents.
        while (queue.nonEmpty) {

            val node = queue.dequeue()

            for (next <- graph(node)) {

                if (!visited(next)) {

                    visited(next) = true

                    depth(next) =
                        depth(node) + 1

                    up(0)(next) = node

                    queue.enqueue(next)
                }
            }
        }

        // Built binary lifting table.
        for (k <- 1 until LOG) {

            for (node <- 1 to n) {

                up(k)(node) =
                    up(k - 1)(
                        up(k - 1)(node)
                    )
            }
        }

        // Precomputed powers of two modulo MOD.
        val pow2 =
            Array.fill(n + 1)(1)

        for (i <- 1 to n) {

            pow2(i) =
                ((pow2(i - 1).toLong * 2)
                    % MOD).toInt
        }

        // Used LCA to find lowest common ancestor.
        def lca(
            startA: Int,
            startB: Int
        ): Int = {

            var a = startA
            var b = startB

            if (depth(a) < depth(b)) {

                val temp = a
                a = b
                b = temp
            }

            val diff =
                depth(a) - depth(b)

            for (k <- 0 until LOG) {

                if ((diff & (1 << k)) != 0) {

                    a = up(k)(a)
                }
            }

            if (a == b) {
                return a
            }

            for (
                k <- (0 until LOG).reverse
            ) {

                if (
                    up(k)(a) != up(k)(b)
                ) {

                    a = up(k)(a)
                    b = up(k)(b)
                }
            }

            up(0)(a)
        }

        // Used answer to store results.
        val answer =
            Array.ofDim[Int](
                queries.length
            )

        // Processed all queries.
        for (
            i <- queries.indices
        ) {

            val u = queries(i)(0)
            val v = queries(i)(1)

            val ancestor =
                lca(u, v)

            // Calculated distance between nodes.
            val dist =
                depth(u) +
                depth(v) -
                2 * depth(ancestor)

            if (dist == 0) {

                answer(i) = 0
            } else {

                // Answer equals 2^(distance - 1).
                answer(i) =
                    pow2(dist - 1)
            }
        }

        // Returned all query answers.
        answer
    }
}