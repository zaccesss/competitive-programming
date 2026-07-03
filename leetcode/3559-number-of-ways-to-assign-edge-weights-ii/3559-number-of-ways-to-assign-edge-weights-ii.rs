impl Solution {
    pub fn assign_edge_weights(
        edges: Vec<Vec<i32>>,
        queries: Vec<Vec<i32>>
    ) -> Vec<i32> {

        const MOD: i64 = 1_000_000_007;

        let n = edges.len() + 1;

        let mut graph = vec![Vec::<usize>::new(); n];

        for e in edges {
            let u = (e[0] - 1) as usize;
            let v = (e[1] - 1) as usize;

            graph[u].push(v);
            graph[v].push(u);
        }

        let log = 18;

        let mut depth = vec![0usize; n];
        let mut up = vec![vec![0usize; n]; log];

        let mut q = std::collections::VecDeque::new();
        q.push_back(0);

        let mut visited = vec![false; n];
        visited[0] = true;

        while let Some(node) = q.pop_front() {

            for &next in &graph[node] {

                if visited[next] {
                    continue;
                }

                visited[next] = true;

                depth[next] = depth[node] + 1;
                up[0][next] = node;

                q.push_back(next);
            }
        }

        for k in 1..log {

            for node in 0..n {

                up[k][node] =
                    up[k - 1][up[k - 1][node]];
            }
        }

        let mut pow2 = vec![1i32; n];

        for i in 1..n {

            pow2[i] =
                ((pow2[i - 1] as i64 * 2) % MOD)
                    as i32;
        }

        let lca = |mut a: usize,
                   mut b: usize,
                   depth: &Vec<usize>,
                   up: &Vec<Vec<usize>>|
         -> usize {

            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }

            let diff = depth[a] - depth[b];

            for k in 0..up.len() {

                if diff & (1 << k) != 0 {
                    a = up[k][a];
                }
            }

            if a == b {
                return a;
            }

            for k in (0..up.len()).rev() {

                if up[k][a] != up[k][b] {

                    a = up[k][a];
                    b = up[k][b];
                }
            }

            up[0][a]
        };

        let mut ans =
            Vec::with_capacity(queries.len());

        for q in queries {

            let u = (q[0] - 1) as usize;
            let v = (q[1] - 1) as usize;

            let p = lca(u, v, &depth, &up);

            let dist =
                depth[u]
                + depth[v]
                - 2 * depth[p];

            if dist == 0 {
                ans.push(0);
            } else {
                ans.push(pow2[dist - 1]);
            }
        }

        ans
    }
}