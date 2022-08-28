#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

int main()
{
    int H1, H2, W1, W2;
    cin >> H1 >> W1;
    vector<vector<int>> A(H1, vector<int>(W1));
    for (vector<int> &a : A) for (int &x : a) cin >> x;
    cin >> H2 >> W2;
    vector<vector<int>> B(H2, vector<int>(W2));
    for (vector<int> &b : B) for (int &x : b) cin >> x;

    for (int i = 1; i < 1 << H1; i++) {
        bitset<10> I(i);
        if (I.count() != H2) continue;
        for (int j = 1; j < 1 << W1; j++) {
            bitset<10> J(j);
            if (J.count() != W2) continue;
            vector<vector<int>> temp(H2, vector<int>(W2));
            int y = 0;
            for (int k = 0; k < H1; k++) {
                int x = 0;
                if (I.test(k)) {
                    for (int l = 0; l < W1; l++) {
                        if (J.test(l)) {
                            temp.at(y).at(x) = A.at(k).at(l);
                            x++;
                        }
                    }
                    y++;
                }
            }
            if (temp == B) {
                cout << "Yes" << endl;
                return 0;
            }
        }
    }
    cout << "No" << endl;

    return 0;
}