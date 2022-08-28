#include <iostream>
#include <vector>
using namespace std;

int main()
{
    string S;
    cin >> S;
    string atcoder = "atcoder";
    vector<int> V(S.size());
    for (int i = 0; i < S.size(); i++) V.at(i) = atcoder.find(S.at(i));

    int ans = 0;
    for (int i = 0; i < S.size(); i++) {
        for (int j = 0; j < S.size() - i - 1; j++) {
            if (V.at(j) > V.at(j + 1)) {
                swap(V.at(j), V.at(j + 1));
                ans++;
            }
        }
    }
    cout << ans << endl;

    return 0;
}