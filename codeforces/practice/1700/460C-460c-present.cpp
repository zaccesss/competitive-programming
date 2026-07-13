#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

int main() {

    int n, m, w;
    cin >> n >> m >> w;

    vector<ll> flowers(n);

    ll minimumHeight = 1e18;
    ll maximumHeight = 0;

    for (int i = 0; i < n; i++) {
        cin >> flowers[i];
        minimumHeight = min(minimumHeight, flowers[i]);
        maximumHeight = max(maximumHeight, flowers[i]);
    }

    auto canMake = [&](ll target) {

        vector<ll> diff(n + 1, 0);

        ll currentAdd = 0;
        ll used = 0;

        for (int i = 0; i < n; i++) {

            currentAdd += diff[i];

            ll currentHeight = flowers[i] + currentAdd;

            if (currentHeight < target) {

                ll need = target - currentHeight;

                used += need;

                if (used > m)
                    return false;

                currentAdd += need;

                if (i + w < n)
                    diff[i + w] -= need;
            }
        }

        return true;
    };

    ll left = minimumHeight;
    ll right = maximumHeight + m;
    ll answer = minimumHeight;

    while (left <= right) {

        ll mid = (left + right) / 2;

        if (canMake(mid)) {
            answer = mid;
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    cout << answer << "\n";

    return 0;
}