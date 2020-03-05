#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void printQuad(int mousePos, int catPos, int mouseMove, int state) {
    cout << " (" << mousePos << ", " 
        << catPos << ", " 
        << (mouseMove ? "M" : "C") << ", "
        << state << ") ";
}

class Solution {
public:
    int catMouseGame(vector<vector<int>>& graph) {
        queue<vector<int>> q;
        int nNodes = graph.size();
        // (mouse pos, cat pos, is mouse move)
        int states[nNodes][nNodes][2];
        for (int i = 0; i < nNodes; i++)
            for (int j = 0; j < nNodes; j++)
                for (int k = 0; k < 2; k++)
                    states[i][j][k] = 0;
        // Cat wins
        for (int i = 1; i < nNodes; i++) {
            q.push({i, i, 0});
            q.push({i, i, 1});
            states[i][i][0] = 2;
            states[i][i][1] = 2;
        }
        // Mouse wins
        for (int i = 0; i < nNodes; i++) {
            q.push({0, i, 0});
            q.push({0, i, 1});
            states[0][i][0] = 1;
            states[0][i][1] = 1;
        }
        while (!q.empty()) {
            vector<int> state = q.front();
            q.pop();
            int mousePos = state[0], catPos = state[1], mouseMove = state[2];
            printQuad(mousePos, catPos, mouseMove, states[mousePos][catPos][mouseMove]);
            cout << "=>";
            if (mouseMove) {
                // Mouse is going to move at this state
                if (states[mousePos][catPos][mouseMove] == 1) {
                    // If mouse wins, mouse would have won at the last step if cat couldn't win
                    for (auto it = graph[catPos].begin(); it != graph[catPos].end(); it++) {
                        bool mouseMustWin = true;
                        for (auto it2 = graph[*it].begin(); it2 != graph[*it].end(); it2++) {
                            if (*it2 != 0 && states[mousePos][*it2][mouseMove] != 1) mouseMustWin = false;
                        }
                        if (mouseMustWin && *it != 0 && states[mousePos][*it][1 - mouseMove] == 0) { 
                            states[mousePos][*it][1 - mouseMove] = 1;
                            q.push({mousePos, *it, 1 - mouseMove});
                            printQuad(mousePos, *it, 1 - mouseMove, 1);
                        }
                    }
                } else if (states[mousePos][catPos][mouseMove] == 2) {
                    // If cat wins, cat could have won at last step
                    for (auto it = graph[catPos].begin(); it != graph[catPos].end(); it++) {
                        if (*it != 0 && states[mousePos][*it][1 - mouseMove] == 0) { 
                            states[mousePos][*it][1 - mouseMove] = 2;
                            q.push({mousePos, *it, 1 - mouseMove});
                            printQuad(mousePos, *it, 1 - mouseMove, 2);
                        }
                    }
                }
            } else {
                // Cat is going to move at this state
                if (states[mousePos][catPos][mouseMove] == 1) {
                    // If mouse wins, mouse could have won at last step
                    for (auto it = graph[mousePos].begin(); it != graph[mousePos].end(); it++) {
                        if (*it != 0 && states[*it][catPos][1 - mouseMove] == 0) {
                            states[*it][catPos][1 - mouseMove] = 1;
                            q.push({*it, catPos, 1 - mouseMove});
                            printQuad(*it, catPos, 1 - mouseMove, 1);
                        }
                    }
                } else if (states[mousePos][catPos][mouseMove] == 2) {
                    // If cat wins, cat would have won at the last step if mouse couldn't win
                    for (auto it = graph[mousePos].begin(); it != graph[mousePos].end(); it++) {
                        bool catMustWin = true;
                        for (auto it2 = graph[*it].begin(); it2 != graph[*it].end(); it2++) {
                            if (*it2 != catPos && states[*it2][catPos][mouseMove] != 2) catMustWin = false;
                        }
                        if (catMustWin && *it != 0 && states[*it][catPos][1 - mouseMove] == 0) {
                            states[*it][catPos][1 - mouseMove] = 2;
                            q.push({*it, catPos, 1 - mouseMove});
                            printQuad(*it, catPos, 1 - mouseMove, 2);
                        }
                    }
                }
            }
            cout << endl;
        }

        for (int i = 0; i < nNodes; i++) {
            for (int j = 0; j < nNodes; j++) {
                cout << states[i][j][0] << "/" << states[i][j][1] << " ";
            }
            cout << endl;
        }
        return states[1][2][1];
    }
};

int main() {
    Solution solution;
    vector<vector<int>> graph;
    graph.push_back({2, 3});
    graph.push_back({3, 4});
    graph.push_back({0, 4});
    graph.push_back({0, 1});
    graph.push_back({1, 2});
    cout << solution.catMouseGame(graph);
    return 0;
}