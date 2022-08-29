#include <iostream>
using namespace std;

int main()
{
    int Y;
    cin >> Y;
    for (int i = Y; i < Y + 4; i++)
    {
        if (i % 4 == 2) cout << i << endl;
    }
    return 0;
}