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

    // case 1:
    // the whole array is one segment.
    if (k == 1) {
        cout << *min_element(a.begin(), a.end()) << endl;
    }

    // case 2:
    // best answer is the larger of the two ends.
    else if (k == 2) {
        cout << max(a[0], a[n - 1]) << endl;
    }

    // case 3:
    // we can isolate the largest element.
    else {
        cout << *max_element(a.begin(), a.end()) << endl;
    }

    return 0;
}