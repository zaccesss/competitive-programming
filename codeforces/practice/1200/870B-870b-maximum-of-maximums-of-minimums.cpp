#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    int n, k;
    cin >> n >> k;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Case 1:
    // The whole array is one segment.
    if (k == 1) {
        cout << *min_element(a.begin(), a.end()) << endl;
    }

    // Case 2:
    // Best answer is the larger of the two ends.
    else if (k == 2) {
        cout << max(a[0], a[n - 1]) << endl;
    }

    // Case 3:
    // We can isolate the largest element.
    else {
        cout << *max_element(a.begin(), a.end()) << endl;
    }

    return 0;
}