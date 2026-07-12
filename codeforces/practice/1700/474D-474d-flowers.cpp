#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAXN = 100000;

int main() {

    int t, k;
    cin >> t >> k;

    vector<long long> dp(MAXN + 1);
    vector<long long> prefix(MAXN + 1);

    // base case
    dp[0] = 1;

    for (int i = 1; i <= MAXN; i++) {

        // end with a red flower
        dp[i] = dp[i - 1];

        // end with a group of k white flowers
        if (i >= k)
            dp[i] = (dp[i] + dp[i - k]) % MOD;
    }

    // prefix[i] = dp[1] + ... + dp[i]
    for (int i = 1; i <= MAXN; i++) {
        prefix[i] = (prefix[i - 1] + dp[i]) % MOD;
    }

    while (t--) {

        int a, b;
        cin >> a >> b;

        cout << (prefix[b] - prefix[a - 1] + MOD) % MOD << "\n";
    }

    return 0;
}