#include <iostream>
using namespace std;

void fibonacci(int n) {
    int re[2] = { 0,0 };
    if (n == 0) {
        cout << 1 << " " << 0 << endl;
    }
    else if (n == 1) {
        cout << 0 << " " << 1 << endl;
    }
    else {
        int pre1[2] = { 0,1 };
        int pre2[2] = { 1,0 };
       
        for (int i = 1; i < n; i++) {
            re[0] = pre1[0] + pre2[0];
            re[1] = pre1[1] + pre2[1];
            pre2[0] = pre1[0];
            pre2[1] = pre1[1];
            pre1[0] = re[0];
            pre1[1] = re[1];
        }
        cout << re[0] << " " << re[1] << endl;
    }
}

int main() {
    int t, n;
    cin >> t;
    while (t > 0) {
        cin >> n;
        fibonacci(n);
        t--;
    }
}
