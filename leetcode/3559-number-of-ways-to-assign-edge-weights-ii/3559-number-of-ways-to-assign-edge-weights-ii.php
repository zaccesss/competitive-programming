class Solution
{

    /**
     * @param Integer[][] $edges
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function assignEdgeWeights($edges, $queries)
    {
        $MOD = 1000000007;
        $LOG = 18;

        $n = count($edges) + 1;

        // Used adjacency list for the tree.
        $graph = array_fill(0, $n + 1, []);

        foreach ($edges as $edge)
        {
            $u = $edge[0];
            $v = $edge[1];

            $graph[$u][] = $v;
            $graph[$v][] = $u;
        }

        // Used depth to store node depths.
        $depth = array_fill(0, $n + 1, 0);

        // Used binary lifting table.
        $up = [];

        for ($i = 0; $i < $LOG; $i++)
        {
            $up[$i] = array_fill(0, $n + 1, 0);
        }

        // Built depths and parents with BFS.
        $queue = [1];

        $visited = array_fill(0, $n + 1, false);

        $visited[1] = true;

        $head = 0;

        while ($head < count($queue))
        {
            $node = $queue[$head++];

            foreach ($graph[$node] as $next)
            {
                if ($visited[$next])
                {
                    continue;
                }

                $visited[$next] = true;

                $depth[$next] = $depth[$node] + 1;

                $up[0][$next] = $node;

                $queue[] = $next;
            }
        }

        // Built binary lifting table.
        for ($k = 1; $k < $LOG; $k++)
        {
            for ($node = 1; $node <= $n; $node++)
            {
                $up[$k][$node] =
                    $up[$k - 1][
                        $up[$k - 1][$node]
                    ];
            }
        }

        // Precomputed powers of 2 modulo MOD.
        $pow2 = array_fill(0, $n + 1, 1);

        for ($i = 1; $i <= $n; $i++)
        {
            $pow2[$i] =
                (int)(
                    ($pow2[$i - 1] * 2)
                    % $MOD
                );
        }

        // Used LCA to find lowest common ancestor.
        $lca = function ($a, $b) use (
            &$depth,
            &$up,
            $LOG
        ) {
            if ($depth[$a] < $depth[$b])
            {
                [$a, $b] = [$b, $a];
            }

            $diff =
                $depth[$a] - $depth[$b];

            for ($k = 0; $k < $LOG; $k++)
            {
                if (
                    ($diff & (1 << $k))
                    != 0
                )
                {
                    $a = $up[$k][$a];
                }
            }

            if ($a == $b)
            {
                return $a;
            }

            for (
                $k = $LOG - 1;
                $k >= 0;
                $k--
            )
            {
                if (
                    $up[$k][$a]
                    != $up[$k][$b]
                )
                {
                    $a = $up[$k][$a];
                    $b = $up[$k][$b];
                }
            }

            return $up[0][$a];
        };

        // Processed all queries.
        $answer = [];

        foreach ($queries as $query)
        {
            $u = $query[0];
            $v = $query[1];

            $ancestor = $lca($u, $v);

            $dist =
                $depth[$u]
                + $depth[$v]
                - 2 * $depth[$ancestor];

            if ($dist == 0)
            {
                $answer[] = 0;
            }
            else
            {
                $answer[] =
                    $pow2[$dist - 1];
            }
        }

        return $answer;
    }
}