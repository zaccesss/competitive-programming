// codeforces 110A - Nearly Lucky Number
// https://codeforces.com/problemset/problem/110/A
// solution by zac
//
//  this code checks if the number of lucky digits (4 or 7)
// in the input number is itself a lucky number (4 or 7).

#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
    cin >> n; // read the number as a string to process each digit
    int lucky_count = 0; // counter for lucky digits

    // loop through each character (digit) in the string
    for (char c : n) {
        if (c == '4' || c == '7') {
            lucky_count++; // increment if digit is lucky
        }
    }

    // check if the count of lucky digits is 4 or 7
    if (lucky_count == 4 || lucky_count == 7) {
        cout << "YES" << endl; // output YES if true
    } else {
        cout << "NO" << endl; // output NO otherwise
    }
    return 0;
}
