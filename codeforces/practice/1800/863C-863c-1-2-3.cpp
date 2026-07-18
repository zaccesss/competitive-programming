#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ll k;
    int a, b;
    cin >> k >> a >> b;

    int A[4][4], B[4][4];

    // Alice's transitions
    for (int i = 1; i <= 3; i++)
        for (int j = 1; j <= 3; j++)
            cin >> A[i][j];

    // Bob's transitions
    for (int i = 1; i <= 3; i++)
        for (int j = 1; j <= 3; j++)
            cin >> B[i][j];

    // First visit time of each state
    int vis[4][4];
    memset(vis, -1, sizeof(vis));

    vector<pair<int, int>> state;
    vector<pair<ll, ll>> pref;
    pref.push_back({0, 0});

    ll alice = 0, bob = 0;
    int step = 0;

    while (step < k && vis[a][b] == -1) {
        vis[a][b] = step;
        state.push_back({a, b});

        // Update score
        if ((a == 1 && b == 3) || (a == 2 && b == 1) || (a == 3 && b == 2))
            alice++;
        else if ((b == 1 && a == 3) || (b == 2 && a == 1) || (b == 3 && a == 2))
            bob++;

        pref.push_back({alice, bob});

        int na = A[a][b];
        int nb = B[a][b];
        a = na;
        b = nb;
        step++;
    }

    if (step == k) {
        cout << alice << " " << bob;
        return 0;
    }

    int start = vis[a][b];
    int len = step - start;

    ll preA = pref[start].first;
    ll preB = pref[start].second;

    ll cycA = pref[step].first - pref[start].first;
    ll cycB = pref[step].second - pref[start].second;

    ll ansA = preA;
    ll ansB = preB;

    ll rem = k - start;

    ansA += (rem / len) * cycA;
    ansB += (rem / len) * cycB;

    rem %= len;

    ansA += pref[start + rem].first - pref[start].first;
    ansB += pref[start + rem].second - pref[start].second;

    cout << ansA << " " << ansB;
}