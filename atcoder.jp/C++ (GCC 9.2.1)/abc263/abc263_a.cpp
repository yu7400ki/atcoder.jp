#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> cnt(13, 0);
    for (int i = 0; i < 5; i++) {
        int x;
        cin >> x;
        cnt.at(x-1)++;
    }

    bool flag = find(cnt.begin(), cnt.end(), 3) != cnt.end() && find(cnt.begin(), cnt.end(), 2) != cnt.end();

    cout << (flag ? "Yes" : "No") << endl;
    return 0;
}