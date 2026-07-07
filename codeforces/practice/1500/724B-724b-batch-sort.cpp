#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n, m;
    cin >> n >> m;

    vector<vector<int>> table(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> table[i][j];
        }
    }

    // try every possible column swap
    for (int c1 = 0; c1 < m; c1++) {
        for (int c2 = c1; c2 < m; c2++) {

            bool possible = true;

            // check every row
            for (int i = 0; i < n && possible; i++) {

                vector<int> row = table[i];

                // apply the chosen column swap
                swap(row[c1], row[c2]);

                vector<int> wrong;

                // find positions that are incorrect
                for (int j = 0; j < m; j++) {
                    if (row[j] != j + 1) {
                        wrong.push_back(j);
                    }
                }

                // more than one row swap would be needed
                if (wrong.size() > 2) {
                    possible = false;
                    break;
                }

                // if exactly two positions are wrong check whether swapping them fixes the row
                if (wrong.size() == 2) {

                    swap(row[wrong[0]], row[wrong[1]]);

                    for (int j = 0; j < m; j++) {
                        if (row[j] != j + 1) {
                            possible = false;
                            break;
                        }
                    }
                }
            }

            if (possible) {
                cout << "YES\n";
                return 0;
            }
        }
    }

    cout << "NO\n";

    return 0;
}