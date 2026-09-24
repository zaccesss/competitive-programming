#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;  // read number of participants and k

    vector<int> scores(n);

    for (int i = 0; i < n; i++) {
        cin >> scores[i];  // read all scores
    }

    int threshold = scores[k - 1];  // get the k-th place score

    int count = 0;  // will count valid participants

    for (int i = 0; i < n; i++) {
        if (scores[i] >= threshold && scores[i] > 0) {
            count++;  // increase count if both conditions are met
        }
    }

    cout << count << endl;  // print the result

    return 0; // end the program
}