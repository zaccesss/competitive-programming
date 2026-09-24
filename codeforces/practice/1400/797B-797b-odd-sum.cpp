#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    int n;
    cin >> n;

    long long sum = 0;

    // smallest positive odd number
    int smallestPositiveOdd = INT_MAX;

    // largest negative odd number (closest to zero)
    int largestNegativeOdd = INT_MIN;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        // take every positive number
        if (x > 0) {
            sum += x;

            // track the smallest positive odd
            if (x % 2 != 0)
                smallestPositiveOdd = min(smallestPositiveOdd, x);
        }

        // track the largest negative odd
        else if (x % 2 != 0) {
            largestNegativeOdd = max(largestNegativeOdd, x);
        }
    }

    // already odd
    if (sum % 2 == 1) {
        cout << sum << "\n";
        return 0;
    }

    long long answer = LLONG_MIN;

    // remove the smallest positive odd
    if (smallestPositiveOdd != INT_MAX)
        answer = max(answer, sum - smallestPositiveOdd);

    // add the largest negative odd
    if (largestNegativeOdd != INT_MIN)
        answer = max(answer, sum + largestNegativeOdd);

    cout << answer << "\n";

    return 0;
}