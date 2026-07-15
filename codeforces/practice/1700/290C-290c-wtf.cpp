#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    long long s = 0, bs = 0, bl = 1;

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        s += x;
        if (s * bl >= 1LL * i * bs)
            bs = s, bl = i;
    }

    cout << fixed << setprecision(6) << (double)bs / bl;
}