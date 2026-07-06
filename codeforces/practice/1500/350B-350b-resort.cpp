#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> type(n + 1);
    for (int i = 1; i <= n; i++)
        cin >> type[i];

    vector<int> parent(n + 1);
    vector<int> out(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> parent[i];

        // Count outgoing tracks
        if (parent[i] != 0)
            out[parent[i]]++;
    }

    vector<int> ans;

    for (int i = 1; i <= n; i++) {
        if (type[i] == 1) {
            vector<int> path;
            int cur = i;

            // Follow the path backwards
            while (cur != 0) {
                path.push_back(cur);

                int prev = parent[cur];

                if (prev != 0 && out[prev] != 1)
                    break;

                cur = prev;
            }

            if (path.size() > ans.size())
                ans = path;
        }
    }

    reverse(ans.begin(), ans.end());

    cout << ans.size() << '\n';
    for (int x : ans)
        cout << x << " ";

    return 0;
}