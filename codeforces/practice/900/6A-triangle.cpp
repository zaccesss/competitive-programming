#include <iostream>
#include <algorithm>
using namespace std;

int main() {

    // used array to store stick lengths.
    int a[4];

    // read all stick lengths.
    for (int i = 0; i < 4; i++) {
        cin >> a[i];
    }

    bool segment = false;

    // checked every combination of three sticks.
    for (int i = 0; i < 4; i++) {

        int sides[3];
        int idx = 0;

        // built current triple.
        for (int j = 0; j < 4; j++) {
            if (j != i) {
                sides[idx++] = a[j];
            }
        }

        // sorted the three sides.
        sort(sides, sides + 3);

        // returned triangle if possible.
        if (sides[0] + sides[1] > sides[2]) {
            cout << "TRIANGLE\n";
            return 0;
        }

        // marked segment if degenerate triangle exists.
        if (sides[0] + sides[1] == sides[2]) {
            segment = true;
        }
    }

    // returned segment if found.
    if (segment) {
        cout << "SEGMENT\n";
    }
    else {
        cout << "IMPOSSIBLE\n";
    }

    return 0;
}