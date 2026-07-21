#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int n;
    cin >> n;
 
    vector<pair<int, int>> seg;
 
    // Read segments
    for (int i = 0; i < n; i++) {
        int l, r;
        cin >> l >> r;
        if (l > r) swap(l, r);
        seg.push_back({r, l});
    }
 
    // Sort by right endpoint
    sort(seg.begin(), seg.end());
 
    vector<int> ans;
    int last = INT_MIN;
 
    for (auto [r, l] : seg) {
        // Already covered
        if (last >= l && last <= r)
            continue;
 
        // Place a new nail
        last = r;
        ans.push_back(last);
    }
 
    cout << ans.size() << '\n';
    for (int x : ans)
        cout << x << " ";
}
