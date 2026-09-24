#include <bits/stdc++.h>
using namespace std;

int main() {

    // used s to store lever description.
    string s;
    cin >> s;

    // used pivot to store position of '^'.
    int pivot = s.find('^');

    // used long long because torques can be large.
    long long leftTorque = 0;
    long long rightTorque = 0;

    // processed every position on the lever.
    for (int i = 0; i < s.size(); i++) {

        // skipped empty positions and pivot.
        if (s[i] == '=' || s[i] == '^') {
            continue;
        }

        // converted digit character to weight.
        int weight = s[i] - '0';

        // added contribution to left side.
        if (i < pivot) {
            leftTorque += 1LL * weight * (pivot - i);
        }

        // added contribution to right side.
        else if (i > pivot) {
            rightTorque += 1LL * weight * (i - pivot);
        }
    }

    // compared both torques.
    if (leftTorque > rightTorque) {
        cout << "left\n";
    }
    else if (rightTorque > leftTorque) {
        cout << "right\n";
    }
    else {
        cout << "balance\n";
    }

    return 0;
}