#include <iostream>
#include <queue>

using namespace std;

int main() {

    int n;
    cin >> n;

    string s;
    cin >> s;

    queue<int> d;
    queue<int> r;

    // stored the positions of each faction
    for (int i = 0; i < n; i++) {
        if (s[i] == 'D')
            d.push(i);
        else
            r.push(i);
    }

    // simulated the voting process
    while (!d.empty() && !r.empty()) {

        int depublican = d.front();
        d.pop();

        int remocrat = r.front();
        r.pop();

        // the earlier employee bans the other
        if (depublican < remocrat)
            d.push(depublican + n);
        else
            r.push(remocrat + n);
    }

    // printed the winner
    if (d.empty())
        cout << "R\n";
    else
        cout << "D\n";

    return 0;
}