#include <iostream>
#include <vector>
using namespace std;

template<typename T>
T binary_search(T ok, T ng, auto key)
{
    while (abs(ok - ng) > 1)
    {
        T mid = (ok + ng) / 2;
        if (key(mid)) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    return ok;
}

int main()
{
    int N;
    long long P, Q, R;
    cin >> N >> P >> Q >> R;
    vector <long long> A(N+1, 0);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i+1);
        A.at(i+1) += A.at(i);
    }

    for (int x = 0; x < N; x++) {
        int y = binary_search(x, N+1, [&](int m)->bool{return A.at(m) - A.at(x) <= P;});
        if (A.at(y) - A.at(x) == P) {
            int z = binary_search(y, N+1, [&](int m)->bool{return A.at(m) - A.at(y) <= Q;});
            if (A.at(z) - A.at(y) == Q) {
                int w = binary_search(z, N+1, [&](int m)->bool{return A.at(m) - A.at(z) <= R;});
                if (A.at(w) - A.at(z) == R) {
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }

    cout << "No" << endl;

    return 0;
}