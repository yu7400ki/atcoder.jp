#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    N--;
    vector<int> P(N);
    for (int &p : P) cin >> p;

    int ans = 0;
    while (1)
    {
        ans++;
        N = P.at(N - 1) - 1;
        if (N == 0) break;
    }

    cout << ans << endl;

    return 0;
}