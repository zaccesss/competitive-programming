#include <bits/stdc++.h>
using namespace std;

int main() {

    // used s to store the input word.
    string s;
    cin >> s;

    // used ok to check if case needs changing.
    bool ok = true;

    // checked if every character after first is uppercase.
    for (int i = 1; i < s.size(); i++) {

        // marked false if lowercase character found.
        if (islower(s[i])) {
            ok = false;
        }
    }

    // changed all character cases if condition passed.
    if (ok) {

        // looped through every character.
        for (int i = 0; i < s.size(); i++) {

            // converted uppercase to lowercase.
            if (isupper(s[i])) {
                s[i] = tolower(s[i]);
            }

            // converted lowercase to uppercase.
            else {
                s[i] = toupper(s[i]);
            }
        }
    }

    // printed final word.
    cout << s << "\n";

    return 0;
}
