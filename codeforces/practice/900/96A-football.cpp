#include <iostream>
#include <string>
using namespace std;

int main() {

    // used s to store player positions.
    string s;
    cin >> s;

    // used streak to track consecutive players.
    int streak = 1;

    // processed the string.
    for (int i = 1; i < s.size(); i++) {

        if (s[i] == s[i - 1]) {
            streak++;
        } else {
            streak = 1;
        }

        // returned YES if dangerous situation found.
        if (streak >= 7) {
            cout << "YES\n";
            return 0;
        }
    }

    // returned NO if no dangerous situation exists.
    cout << "NO\n";

    return 0;
}