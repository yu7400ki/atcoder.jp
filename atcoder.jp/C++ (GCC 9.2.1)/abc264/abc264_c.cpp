#include <iostream>
#include <vector>
#include <cmath>
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

    for (int i = 1; i < pow(2, H1); i++) {
        for (int j = 1; j < pow(2, W1); j++) {
            vector<vector<int>> temp;
            for (int k = 0; k < H1; k++) {
                if (i >> k & 1) {
                    vector<int> temp_h;
                    for (int l = 0; l < W1; l++) {
                        if (j >> l & 1) {
                            temp_h.push_back(A.at(k).at(l));
                        }
                    }
                    temp.push_back(temp_h);
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