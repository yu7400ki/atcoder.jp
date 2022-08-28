#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main()
{
    int N, M, T;
    cin >> N >> M >> T;
    vector<int> A(N-1, 0);
    unordered_map<int, int> bonus;
    for (int &a : A) cin >> a;
    for (int i = 0; i < M; i++) 
    {
        int X, Y;
        cin >> X >> Y;
        bonus.emplace(X, Y);
    }

    int pos = 1;
    for (int a : A)
    {
        if (T - a > 0) {
            T -= a;
            pos++;
        } else {
            cout << "No" << endl;
            return 0;
        }

        if (bonus.count(pos) > 0) {
            T += bonus.at(pos);
        }
    }

    cout << "Yes" << endl;

    return 0;
}