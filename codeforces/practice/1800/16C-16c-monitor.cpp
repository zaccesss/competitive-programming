#include <iostream>
#include <algorithm>

using namespace std;

using int64 = long long;

int64 gcd(int64 a, int64 b) {
    while (b) {
        int64 t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {

    int64 a, b, x, y;
    cin >> a >> b >> x >> y;

    int64 g = gcd(x, y);
    x /= g;
    y /= g;

    int64 scale = min(a / x, b / y);

    if (scale == 0) {
        cout << "0 0\n";
    }
    else {
        cout << x * scale << " " << y * scale << "\n";
    }

    return 0;
}