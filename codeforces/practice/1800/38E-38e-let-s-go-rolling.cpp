#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

const ll INF = (1LL << 60);

int main() {

    int n;
    cin >> n;

    vector<pair<ll, ll>> a(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> a[i].first >> a[i].second;
    }

    // sort the marbles by position
    sort(a.begin() + 1, a.end());

    // dp[i][j] = minimum cost after processing i marbles
    // where j is the last pinned marble
    vector<vector<ll>> dp(n + 2, vector<ll>(n + 2, INF));

    // the first marble must be pinned
    dp[1][1] = a[1].second;

    for (int i = 2; i <= n; i++) {

        for (int last = 1; last < i; last++) {

            if (dp[i - 1][last] == INF)
                continue;

            // pin the current marble
            dp[i][i] = min(dp[i][i],
                           dp[i - 1][last] + a[i].second);

            // let the current marble roll
            dp[i][last] = min(dp[i][last],
                              dp[i - 1][last] +
                              (a[i].first - a[last].first));
        }
    }

    ll ans = INF;

    // find the best final answer
    for (int last = 1; last <= n; last++) {
        ans = min(ans, dp[n][last]);
    }

    cout << ans << "\n";

    return 0;
}