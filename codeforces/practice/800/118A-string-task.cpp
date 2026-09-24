#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;  // read the input word

    // these are all the vowels we want to remove.
    // note: 'y' is also treated as a vowel in this problem.
    string vowels = "aeiouy";

    for (char ch : s) {
        char lower = tolower(ch);  // convert each character to lowercase first

        // only print the character if it is NOT a vowel.
        // the problem also requires a dot '.' printed before each consonant.
        if (vowels.find(lower) == string::npos) {
            cout << '.' << lower;
        }
    }

    cout << '\n';
    return 0;
}
