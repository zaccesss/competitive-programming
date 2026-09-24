#include <bits/stdc++.h>
using namespace std;

int main() {

    // used n for poster length and k for ladder position.
    int n, k;
    cin >> n >> k;

    // used slogan to store poster text.
    string slogan;
    cin >> slogan;

    // moved to left end if closer to left side.
    if (k <= (n + 1) / 2) {

        // moved ladder to position 1.
        while (k > 1) {
            cout << "LEFT\n";
            k--;
        }

        // printed characters from left to right.
        for (int i = 0; i < n; i++) {

            cout << "PRINT " << slogan[i] << "\n";

            if (i < n - 1) {
                cout << "RIGHT\n";
            }
        }
    }

    // otherwise moved to right end.
    else {

        // moved ladder to position n.
        while (k < n) {
            cout << "RIGHT\n";
            k++;
        }

        // printed characters from right to left.
        for (int i = n - 1; i >= 0; i--) {

            cout << "PRINT " << slogan[i] << "\n";

            if (i > 0) {
                cout << "LEFT\n";
            }
        }
    }

    return 0;
}