#include <bits/stdc++.h>
using namespace std;

int main() {

    // used k to store required flower growth.
    int k;
    cin >> k;

    // returned 0 if no growth was needed.
    if (k == 0) {
        cout << 0 << "\n";
        return 0;
    }

    // used months to store monthly growth values.
    vector<int> months(12);

    // read all monthly growth values.
    for (int i = 0; i < 12; i++) {
        cin >> months[i];
    }

    // sorted growth values in descending order.
    sort(months.begin(), months.end(), greater<int>());

    // used total to track accumulated growth.
    int total = 0;

    // used count to track months used.
    int count = 0;

    // looped through sorted growth values.
    for (int growth : months) {

        // added current month's growth.
        total += growth;

        // increased month count.
        count++;

        // returned answer once target was reached.
        if (total >= k) {
            cout << count << "\n";
            return 0;
        }
    }

    // printed -1 if target growth was impossible.
    cout << -1 << "\n";

    return 0;
}
