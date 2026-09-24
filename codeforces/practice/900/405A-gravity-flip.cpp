#include <bits/stdc++.h>
using namespace std;

int main() {

    // used n to store number of columns.
    int n;
    cin >> n;

    // used heights to store column heights.
    vector<int> heights(n);

    // read all column heights.
    for (int i = 0; i < n; i++) {
        cin >> heights[i];
    }

    // sorted heights in ascending order.
    sort(heights.begin(), heights.end());

    // printed sorted heights.
    for (int i = 0; i < n; i++) {
        cout << heights[i];

        if (i < n - 1) {
            cout << " ";
        }
    }

    cout << "\n";

    return 0;
}