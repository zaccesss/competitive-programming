#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    int n, m;
    cin >> n >> m;

    vector<int> f(m);

    for (int i = 0; i < m; i++) {
        cin >> f[i];
    }

    // sorted puzzle sizes.
    sort(f.begin(), f.end());

    // used answer to store minimum difference.
    int answer = INT_MAX;

    // checked every window of size n.
    for (int i = 0; i + n - 1 < m; i++) {

        answer = min(
            answer,
            f[i + n - 1] - f[i]
        );
    }

    cout << answer << '\n';

    return 0;
}