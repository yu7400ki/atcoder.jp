#include <iostream>
using namespace std;

int main()
{
    long long int N;
    cin >> N;
    long long int ans = N % 998244353;
    if (ans < 0) ans += 998244353;
    cout << ans << endl;
    return 0;
}