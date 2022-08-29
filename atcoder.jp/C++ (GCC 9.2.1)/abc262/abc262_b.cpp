#include <iostream>
#include <unordered_set>
#include <unordered_map>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    unordered_map<int, unordered_set<int>> graph;
    for (int i = 0; i < M; i++)
    {
        int U, V;
        cin >> U >> V;
        if (graph.contains(U)) graph.at(U).emplace(V); else graph.emplace(U, unordered_set<int>{V});
        if (graph.contains(V)) graph.at(V).emplace(U); else graph.emplace(V, unordered_set<int>{U});
    }

    int cnt = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = i+1; j <= N; j++) {
            for (int k = j+1; k <= N; k++) {
                if (graph.contains(i) && graph.contains(j) && graph.contains(k)) {
                    if (graph.at(i).contains(j) && graph.at(j).contains(k) && graph.at(k).contains(i)) {
                        cnt++;
                    }
                }
            }
        }
    }
    
    cout << cnt << endl;

    return 0;
}
