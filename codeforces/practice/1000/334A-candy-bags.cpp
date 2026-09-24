#include <bits/stdc++.h>
using namespace std;

int main() {

    // used n to store number of brothers.
    int n;
    cin >> n;

    // used left and right pointers for smallest and largest bags.
    int left = 1;
    int right = n * n;

    // looped through every brother.
    for (int i = 0; i < n; i++) {

        // gave each brother n / 2 pairs of bags.
        for (int j = 0; j < n / 2; j++) {

            // printed smallest remaining bag.
            cout << left << " ";

            // printed largest remaining bag.
            cout << right << " ";

            // moved both pointers.
            left++;
            right--;
        }

        // moved to next brother line.
        cout << "\n";
    }

    return 0;
}
