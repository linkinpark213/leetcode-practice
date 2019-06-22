//
// Created by linkinpark213 on 6/22/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>> &matrix) {
        vector<int> ans;
        if (matrix.empty())
            return ans;
        int M = matrix.size();
        int N = matrix[0].size();
        int r, l;
        for (int i = 0; i < M + N - 1; i++) {
            l = max(0, i - M + 1);
            r = min(i + 1, N);
            if (i % 2 == 0) {
                for (int j = l; j < r; j++) {
                    ans.push_back(matrix[i - j][j]);
                }
            } else {
                for (int j = r - 1; j >= l; j--) {
                    ans.push_back(matrix[i - j][j]);
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    int numbers1[] = {1, 2, 3, 4};
    int numbers2[] = {5, 6, 7, 8};
    int numbers3[] = {9, 10, 11, 12};
    vector<int> row1(numbers1, numbers1 + sizeof(numbers1) / sizeof(int));
    vector<int> row2(numbers2, numbers2 + sizeof(numbers2) / sizeof(int));
    vector<int> row3(numbers3, numbers3 + sizeof(numbers3) / sizeof(int));
    vector<vector<int>> matrix;
    matrix.push_back(row1);
    matrix.push_back(row2);
    matrix.push_back(row3);
    vector<int> ans = solution.findDiagonalOrder(matrix);
    for (const auto& v : matrix) {
        for (int i : v)
            cout << i << " ";
        cout << endl;
    }
    for (int i : ans) cout << i << ' ';
}
