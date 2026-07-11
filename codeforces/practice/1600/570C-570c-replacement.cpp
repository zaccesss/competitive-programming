#include <iostream>
#include <string>

using namespace std;

int main() {

    int n, m;
    cin >> n >> m;

    string s;
    cin >> s;

    int answer = 0;

    // counted the initial adjacent dot pairs
    for (int i = 1; i < n; i++) {
        if (s[i] == '.' && s[i - 1] == '.')
            answer++;
    }

    while (m--) {

        int pos;
        char ch;
        cin >> pos >> ch;
        pos--;

        // removed the old contribution
        if (pos > 0 && s[pos] == '.' && s[pos - 1] == '.')
            answer--;

        if (pos + 1 < n && s[pos] == '.' && s[pos + 1] == '.')
            answer--;

        // updated the character
        s[pos] = ch;

        // added the new contribution
        if (pos > 0 && s[pos] == '.' && s[pos - 1] == '.')
            answer++;

        if (pos + 1 < n && s[pos] == '.' && s[pos + 1] == '.')
            answer++;

        cout << answer << "\n";
    }

    return 0;
}