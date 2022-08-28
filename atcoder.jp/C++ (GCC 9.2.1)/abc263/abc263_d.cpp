#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N, L, R;
    cin >> N >> L >> R;
    vector<int> A(N);
    for (int &a : A) cin >> a;

    long long A_sum = 0;
    for (int a : A) A_sum += a;

    vector<long long> R_d(N+1, 0);
    vector<long long> L_d(N+1, 0);
    for (int i = 0; i < N; i++) R_d.at(i+1) = L - A.at(i) + R_d.at(i);
    for (int i = N-1; i >= 0; i--) L_d.at(i) = R - A.at(i) + L_d.at(i+1);
    
    long long mi = 0;
    for (int i = N; i >= 0; i--) {
        mi = min(mi, L_d.at(i));
        L_d.at(i) = mi;
    }

    long long ans = (long long)1 << 62;
    for (int i = 0; i <= N; i++) ans = min(ans, R_d.at(i) + L_d.at(i));

    cout << A_sum + ans << endl;
    
    return 0;
}