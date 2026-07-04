#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int main() {
    int n, l, r;
    cin >> n >> l >> r;
 
    // Convert to 0-based indexing
    l--;
    r--;
 
    vector<int> a(n), b(n);
 
    for (int i = 0; i < n; i++)
        cin >> a[i];
 
    for (int i = 0; i < n; i++)
        cin >> b[i];
 
    // Elements before l must remain unchanged
    for (int i = 0; i < l; i++) {
        if (a[i] != b[i]) {
            cout << "LIE\n";
            return 0;
        }
    }
 
    // Elements after r must remain unchanged
    for (int i = r + 1; i < n; i++) {
        if (a[i] != b[i]) {
            cout << "LIE\n";
            return 0;
        }
    }
 
    // Extract the subarrays that may have been reordered
    vector<int> firstSegment;
    vector<int> secondSegment;
 
    for (int i = l; i <= r; i++) {
        firstSegment.push_back(a[i]);
        secondSegment.push_back(b[i]);
    }
 
    // Order inside the segment does not matter
    sort(firstSegment.begin(), firstSegment.end());
    sort(secondSegment.begin(), secondSegment.end());
 
    if (firstSegment == secondSegment)
        cout << "TRUTH\n";
    else
        cout << "LIE\n";
 
    return 0;
}