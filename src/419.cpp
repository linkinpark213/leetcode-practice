//
// Created by linkinpark213 on 5/14/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
    int countBattleships(vector<vector<char>> &board) {
        int count = 0;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                if (board[i][j] == 'X' && (i == 0 || board[i - 1][j] == '.') && (j == 0 || board[i][j - 1] == '.'))
                    count++;
            }
        }
        return count;
    }
};

int main() {
    Solution solution;
    char line1[] = {'X', '.', '.', 'X'};
    char line2[] = {'.', '.', '.', 'X'};
    char line3[] = {'.', 'X', '.', 'X'};
    vector<char> vector1(line1, line1 + sizeof(line1) / sizeof(char));
    vector<char> vector2(line2, line2 + sizeof(line2) / sizeof(char));
    vector<char> vector3(line3, line3 + sizeof(line3) / sizeof(char));
    vector<char> array[] = {vector1, vector2, vector3};
    vector<vector<char>> board(array, array + sizeof(array) / sizeof(vector<char>));
    cout << solution.countBattleships(board);
}