#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N, last;
    cin >> N;
    unordered_map<int, int> X;
    unordered_map<int, int> A;
    for (int i = 0; i < N; i++)
    {
        int t, x, a;
        cin >> t >> x >> a;
        X.emplace(t, x);
        A.emplace(t, a);
        if (i == N-1) last = t;
    }

    vector<vector<long long>> dp(last+1, vector<long long>(5, 0));
    for (int i = 0; i < last; i++)
    {
        for (int j = 0; j < min(i+1, 5); j++)
        {
            dp.at(i+1).at(j) = max(dp.at(i+1).at(j), dp.at(i).at(j) + (X.count(i+1) > 0 && X.at(i+1) == j ? A.at(i+1) : 0));
            if (j > 0) {
                dp.at(i+1).at(j-1) = max(dp.at(i+1).at(j-1), dp.at(i).at(j) + (X.count(i+1) > 0 && X.at(i+1) == j-1 ? A.at(i+1) : 0));
            }
            if (j < 4) {
                dp.at(i+1).at(j+1) = max(dp.at(i+1).at(j+1), dp.at(i).at(j) + (X.count(i+1) > 0 && X.at(i+1) == j+1 ? A.at(i+1) : 0));
            }
        }
    }

    long long ans = *max_element(dp.back().begin(), dp.back().end());
    cout << ans << endl;

    return 0;
}