#include <bits/stdc++.h>
using namespace std;

using pii = pair<int, int>;

int solve(vector<pii> &v, int budget) {
    // Keep only affordable fountains
    vector<pii> a;
    for (auto &x : v)
        if (x.first <= budget)
            a.push_back(x);

    if (a.size() < 2)
        return 0;

    // Sort by cost
    sort(a.begin(), a.end());

    int m = a.size();

    // Prefix maximum beauty
    vector<int> pre(m);
    pre[0] = a[0].second;
    for (int i = 1; i < m; i++)
        pre[i] = max(pre[i - 1], a[i].second);

    int ans = 0;

    for (int i = 1; i < m; i++) {
        int rem = budget - a[i].first;

        // Find last fountain before i within remaining budget
        int pos = upper_bound(a.begin(), a.begin() + i, make_pair(rem, INT_MAX))
                  - a.begin() - 1;

        if (pos >= 0)
            ans = max(ans, a[i].second + pre[pos]);
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, c, d;
    cin >> n >> c >> d;

    vector<pii> coin, dia;
    int bestCoin = 0, bestDia = 0;

    for (int i = 0; i < n; i++) {
        int b, p;
        char t;
        cin >> b >> p >> t;

        if (t == 'C') {
            coin.push_back({p, b});
            if (p <= c)
                bestCoin = max(bestCoin, b);
        } else {
            dia.push_back({p, b});
            if (p <= d)
                bestDia = max(bestDia, b);
        }
    }

    int ans = 0;

    // One coin + one diamond
    if (bestCoin && bestDia)
        ans = bestCoin + bestDia;

    // Two coins
    ans = max(ans, solve(coin, c));

    // Two diamonds
    ans = max(ans, solve(dia, d));

    cout << ans << '\n';

    return 0;
}