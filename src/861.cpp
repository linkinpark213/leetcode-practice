//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {

    int columnSum(vector<vector<int>> &A, int column) {
        int sum = 0;
        for (auto &i : A) {
            sum += i[column];
        }
        return sum;
    }

    void rowFlip(vector<vector<int>> &A, int row) {
        for (int &i : A[row]) {
            i = 1 - i;
        }
    }

    void columnFlip(vector<vector<int>> &A, int column) {
        for (auto &i : A) {
            i[column] = 1 - i[column];
        }
    }

    int sum(vector<vector<int>> &A) {
        int exp = 1;
        int sum = 0;
        for (int i = A[0].size() - 1; i >= 0; i--) {
            sum += columnSum(A, i) * exp;
            exp *= 2;
        }
        return sum;
    }

public:
    int matrixScore(vector<vector<int>> &A) {
        for (int row = 0; row < A.size(); row++) {
            if (A[row][0] == 0)
                rowFlip(A, row);
        }
        int rowNum = A.size();
        for (int column = 1; column < A[0].size(); column++) {
            if (columnSum(A, column) * 2 < rowNum)
                columnFlip(A, column);
        }
        return sum(A);
    }
};

int main() {
    Solution solution;
    int a1[] = {0, 0, 1, 1};
    int a2[] = {1, 0, 1, 0};
    int a3[] = {1, 1, 0, 0};
    vector<int> v1(a1, a1 + sizeof(a1) / sizeof(int));
    vector<int> v2(a2, a2 + sizeof(a2) / sizeof(int));
    vector<int> v3(a3, a3 + sizeof(a3) / sizeof(int));
    vector<vector<int>> A;
    A.push_back(v1);
    A.push_back(v2);
    A.push_back(v3);
    cout << solution.matrixScore(A);
}