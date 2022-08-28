#include <iostream>
#include <vector>
#include <set>
#include <utility>
using namespace std;

int main()
{
    int H, W;
    cin >> H >> W;
    vector<string> G(H);
    for (string &g : G) cin >> g;
    pair<int, int> pos = {0, 0};
    set<pair<int, int>> seen{pos};

    while (1)
    {
        char s = G.at(pos.first).at(pos.second);
        if (s == 'U') {
            pos.first--;
        } else if (s == 'D') {
            pos.first++;
        } else if (s == 'L') {
            pos.second--;
        } else if (s == 'R') {
            pos.second++;
        } else {
            break;
        }

        if (pos.first < 0 || pos.first >= H || pos.second < 0 || pos.second >= W) {
            if (pos.first < 0) pos.first = 0;
            if (pos.first >= H) pos.first = H - 1;
            if (pos.second < 0) pos.second = 0;
            if (pos.second >= W) pos.second = W - 1;
            cout << pos.first+1 << " " << pos.second+1 << endl;
            break;
        }

        if (seen.count(pos) > 0) {
            cout << -1 << endl;
            break;
        }

        seen.emplace(pos);
    }

    return 0;
}