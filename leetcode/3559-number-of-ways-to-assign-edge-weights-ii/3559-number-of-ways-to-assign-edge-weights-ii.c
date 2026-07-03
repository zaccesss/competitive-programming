/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#define MOD 1000000007LL
#define LOG 18

static int depthArr[100005];
static int up[18][100005];
static int pow2Arr[100005];

int lca(int a, int b)
{
    if (depthArr[a] < depthArr[b])
    {
        int temp = a;
        a = b;
        b = temp;
    }

    int diff = depthArr[a] - depthArr[b];

    for (int k = 0; k < LOG; k++)
    {
        if (diff & (1 << k))
        {
            a = up[k][a];
        }
    }

    if (a == b)
    {
        return a;
    }

    for (int k = LOG - 1; k >= 0; k--)
    {
        if (up[k][a] != up[k][b])
        {
            a = up[k][a];
            b = up[k][b];
        }
    }

    return up[0][a];
}

int* assignEdgeWeights(
    int** edges,
    int edgesSize,
    int* edgesColSize,
    int** queries,
    int queriesSize,
    int* queriesColSize,
    int* returnSize
) {
    int n = edgesSize + 1;

    *returnSize = queriesSize;

    /* Used adjacency list for the tree. */
    int* head = malloc((n + 1) * sizeof(int));
    int* to = malloc((2 * edgesSize) * sizeof(int));
    int* next = malloc((2 * edgesSize) * sizeof(int));

    for (int i = 0; i <= n; i++)
    {
        head[i] = -1;
    }

    int idx = 0;

    for (int i = 0; i < edgesSize; i++)
    {
        int u = edges[i][0];
        int v = edges[i][1];

        to[idx] = v;
        next[idx] = head[u];
        head[u] = idx++;

        to[idx] = u;
        next[idx] = head[v];
        head[v] = idx++;
    }

    /* Used BFS to build depths and parents. */
    int* queue = malloc((n + 5) * sizeof(int));

    int front = 0;
    int rear = 0;

    int* visited = calloc(n + 1, sizeof(int));

    queue[rear++] = 1;
    visited[1] = 1;

    depthArr[1] = 0;
    up[0][1] = 0;

    while (front < rear)
    {
        int node = queue[front++];

        for (int e = head[node]; e != -1; e = next[e])
        {
            int nxt = to[e];

            if (visited[nxt])
            {
                continue;
            }

            visited[nxt] = 1;

            depthArr[nxt] = depthArr[node] + 1;

            up[0][nxt] = node;

            queue[rear++] = nxt;
        }
    }

    /* Built binary lifting table. */
    for (int k = 1; k < LOG; k++)
    {
        for (int node = 1; node <= n; node++)
        {
            up[k][node] =
                up[k - 1][
                    up[k - 1][node]
                ];
        }
    }

    /* Precomputed powers of two modulo MOD. */
    pow2Arr[0] = 1;

    for (int i = 1; i <= n; i++)
    {
        pow2Arr[i] =
            (int)((2LL * pow2Arr[i - 1]) % MOD);
    }

    /* Used answer to store query results. */
    int* answer = malloc(queriesSize * sizeof(int));

    for (int i = 0; i < queriesSize; i++)
    {
        int u = queries[i][0];
        int v = queries[i][1];

        int ancestor = lca(u, v);

        int dist =
            depthArr[u]
            + depthArr[v]
            - 2 * depthArr[ancestor];

        /* Added zero for empty paths. */
        if (dist == 0)
        {
            answer[i] = 0;
        }
        else
        {
            answer[i] = pow2Arr[dist - 1];
        }
    }

    free(head);
    free(to);
    free(next);
    free(queue);
    free(visited);

    return answer;
}