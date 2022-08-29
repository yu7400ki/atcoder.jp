#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    for (int &a : A) cin >> a;

    int cnt = 0;
    int ans = 0;
    for (int j = 1; j <= N; j++) {
        if (j == A.at(j-1)) {
            ans += cnt;
            cnt++;
        } else {
            int i = A.at(j-1);
            if (min(A.at(i-1), A.at(j-1)) == i && max(A.at(i-1), A.at(j-1)) == j) {
                ans++;
            }
        }
    }

    cout << ans << endl;

    return 0;
}