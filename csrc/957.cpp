//
// Created by linkinpark213 on 5/14/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> prisonAfterNDays(vector<int> &cells, int N) {
        if (N == 0)
            return cells;
        vector<int> newCells(8, 0);
        // A cycle is 14 days
        N = N % 14;
        if (N == 0) N = 14;
        for (int i = 1; i < cells.size() - 1; i++) {
            if (cells[i - 1] == cells[i + 1])
                newCells[i] = 1;
        }
        return prisonAfterNDays(newCells, N - 1);
    }
};

int main() {
    Solution solution;
    int array[] = {1, 0, 0, 1, 0, 0, 1, 0};
    vector<int> cells(array, array + sizeof(array) / sizeof(int));
    for (int i : solution.prisonAfterNDays(cells, 1000000000))
        cout << i << ' ';
}