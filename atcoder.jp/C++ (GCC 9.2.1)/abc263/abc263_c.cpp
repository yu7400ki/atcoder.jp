#include <iostream>
#include <vector>
using namespace std;

void bfs(vector<int> &A, int &N, int &M) {
    if (A.size() == N) {
        for (int &a : A) cout << a << " ";
        cout << endl;
        return;
    }

    int s = A.size() == 0 ? 1 : A.back() + 1;
    for (int i = s; i <= M; i++) {
        A.push_back(i);
        bfs(A, N, M);
        A.pop_back();
    }
}

int main()
{
    int N, M;
    cin >> N >> M;
    vector<int> A;
    bfs(A, N, M);
    return 0;
}