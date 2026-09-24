#include <bits/stdc++.h>
using namespace std;

int main() {

    // used n to store number of cars.
    int n;
    cin >> n;

    // used goodCars to store good car indices.
    vector<int> goodCars;

    // processed each car.
    for (int i = 0; i < n; i++) {

        // used good to track whether current car is good.
        bool good = true;

        // read collision results for current row.
        for (int j = 0; j < n; j++) {

            int x;
            cin >> x;

            // marked car as bad if it turned over.
            if (x == 1 || x == 3) {
                good = false;
            }
        }

        // added car index if it was good.
        if (good) {
            goodCars.push_back(i + 1);
        }
    }

    // printed number of good cars.
    cout << goodCars.size() << "\n";

    // printed good car indices.
    for (int car : goodCars) {
        cout << car << " ";
    }

    cout << "\n";

    return 0;
}