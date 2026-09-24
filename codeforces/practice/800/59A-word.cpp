// codeforces 59A - Word
// https://codeforces.com/problemset/problem/59/A
// solution by zac
//
// this code counts how many uppercase and lowercase letters are in the word.
// then it changes the whole word to the case that appears more often.
// if both counts are the same, Codeforces wants the word in lowercase.

#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    cin >> word; // read the word

    int uppercase = 0; // counter for uppercase letters
    int lowercase = 0; // counter for lowercase letters

    // loop through every character in the word
    for (char c : word) {
        if (isupper(static_cast<unsigned char>(c))) {
            uppercase++; // add 1 if the character is uppercase
        } else {
            lowercase++; // otherwise, it is lowercase
        }
    }

    // if there are more uppercase letters, convert the whole word to uppercase
    if (uppercase > lowercase) {
        transform(word.begin(), word.end(), word.begin(), [](unsigned char c) {
            return static_cast<char>(toupper(c));
        });
    } else {
        // if lowercase is more common or counts are tied, convert to lowercase
        transform(word.begin(), word.end(), word.begin(), [](unsigned char c) {
            return static_cast<char>(tolower(c));
        });
    }

    cout << word << endl; // print the final converted word
    return 0; // program finished successfully
}
