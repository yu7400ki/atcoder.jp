#include <iostream>
using namespace std;

int main()
{
    int R, C;
    cin >> R >> C;
    R = abs(R - 8);
    C = abs(C - 8);
    cout << (max(R, C) % 2 == 0 ? "white" : "black") << endl;
    return 0;
}