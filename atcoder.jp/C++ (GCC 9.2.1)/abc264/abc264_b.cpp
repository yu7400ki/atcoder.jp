#include <iostream>
using namespace std;

int main()
{
    int R, C;
    cin >> R >> C;
    R = 7 - R + 1;
    C -= 8;
    cout << (max(R, C) % 2 == 0 ? "white" : "black") << endl;
    return 0;
}