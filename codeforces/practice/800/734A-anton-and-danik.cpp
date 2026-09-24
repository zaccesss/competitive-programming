// codeforces 734A - Anton and Danik
// https://codeforces.com/problemset/problem/734/A
// solution by zac
//
// this code counts how many games Anton and Danik won.
// then it prints the player with more wins or "Friendship" if tied.

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n; // read how many games were played

    string games;
    cin >> games; // read the string of winners

    int anton_wins = 0; // counter for Anton's wins
    int danik_wins = 0; // counter for Danik's wins

    // loop through each game result
    for (char winner : games) {
        if (winner == 'A') {
            anton_wins++; // anton won this game
        } else {
            danik_wins++; // danik won this game
        }
    }

    // compare the win counts and print the result
    if (anton_wins > danik_wins) {
        cout << "Anton" << endl;
    } else if (danik_wins > anton_wins) {
        cout << "Danik" << endl;
    } else {
        cout << "Friendship" << endl;
    }

    return 0; // program finished successfully
}
