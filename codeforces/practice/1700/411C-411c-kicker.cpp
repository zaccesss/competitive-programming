#include <bits/stdc++.h>
using namespace std;

// Check if team a beats team b
bool win(pair<int,int> a, pair<int,int> b) {
    return a.first > b.second && a.second > b.first;
}

int main() {
    int a[5], b[5];

    // Read defence and attack skills
    for (int i = 1; i <= 4; i++)
        cin >> a[i] >> b[i];

    // Team 1's two possible arrangements
    pair<int,int> t1[2] = {
        {a[2], b[1]},
        {a[1], b[2]}
    };

    // Team 2's two possible arrangements
    pair<int,int> t2[2] = {
        {a[4], b[3]},
        {a[3], b[4]}
    };

    bool ok1 = false;

    // Can Team 1 guarantee a win?
    for (int i = 0; i < 2; i++) {
        bool good = true;
        for (int j = 0; j < 2; j++)
            if (!win(t1[i], t2[j]))
                good = false;
        if (good) ok1 = true;
    }

    if (ok1) {
        cout << "Team 1";
        return 0;
    }

    bool ok2 = true;

    // Can Team 2 always find a winning response?
    for (int i = 0; i < 2; i++) {
        bool good = false;
        for (int j = 0; j < 2; j++)
            if (win(t2[j], t1[i]))
                good = true;
        if (!good) ok2 = false;
    }

    if (ok2) cout << "Team 2";
    else cout << "Draw";
}