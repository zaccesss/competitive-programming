#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    // Handle small cases separately
    if (n == 1) {
        cout << 1 << "\n";
        cout << 1 << "\n";
        return 0;
    }

    if (n == 2) {
        cout << 1 << "\n";
        cout << 1 << "\n";
        return 0;
    }

    if (n == 3) {
        cout << 2 << "\n";
        cout << "1 3\n";
        return 0;
    }

    // For n >= 4, we can use all students
    cout << n << "\n";

    // Print all even numbers first
    for (int i = 2; i <= n; i += 2) {
        cout << i << " ";
    }

    // Then print all odd numbers
    for (int i = 1; i <= n; i += 2) {
        cout << i << " ";
    }

    cout << "\n";

    return 0;
}