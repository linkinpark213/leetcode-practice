//
// Created by linkinpark213 on 6/4/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int threeSumMulti(vector<int> &A, int target) {
        for (int i = 0; i < A.size(); i++) {
            for (int j = A.size() - 1; j > i; j--) {
                if (A[j] < A[j - 1]) {
                    int temp = A[j];
                    A[j] = A[j - 1];
                    A[j - 1] = temp;
                }
            }
        }
        vector<int> noRepeat;
        vector<long> repetition;
        int temp = -1;
        int time = 0;
        for (int i : A) {
            if (i == temp) {
                time += 1;
            } else {
                if (time > 0) {
                    noRepeat.push_back(temp);
                    repetition.push_back(time);
                }
                time = 1;
                temp = i;
            }
        }
        if (time > 0) {
            noRepeat.push_back(temp);
            repetition.push_back(time);
        }

        long sum = 0;
        for (int i = 0; i < noRepeat.size(); i++) {
            for (int j = noRepeat.size() - 1; j >= i; j--) {
                if (i == j && repetition[i] < 3) break;
                for (int k = i; k <= j; k++) {
                    if (noRepeat[i] + noRepeat[j] + noRepeat[k] == target) {
                        if (i == j && i == k) {
                            sum += (repetition[i] * (repetition[i] - 1) * (repetition[i] - 2) / 6);
                        } else if (i == k) {
                            sum += ((repetition[i] * (repetition[i] - 1)) / 2) * repetition[j];
                        } else if (k == j) {
                            sum += repetition[i] * (repetition[j] * (repetition[j] - 1) / 2);
                        } else {
                            sum += repetition[i] * repetition[j] * repetition[k];
                        }
                    }
                }
            }
            if (sum >= 1000000007) sum %= 1000000007;
        }
        return sum;
    }
};

int main() {
    Solution solution;
    vector<int> A;
    A.push_back(1);
    A.push_back(1);
    A.push_back(2);
    A.push_back(2);
    A.push_back(3);
    A.push_back(3);
    A.push_back(4);
    A.push_back(4);
    A.push_back(5);
    A.push_back(5);
    cout << solution.threeSumMulti(A, 8) << endl;

    vector<int> B;
    B.push_back(0);
    B.push_back(0);
    B.push_back(0);
    B.push_back(0);
    B.push_back(0);
    B.push_back(0);
    B.push_back(0);
    B.push_back(0);
    B.push_back(0);
    cout << solution.threeSumMulti(B, 0) << endl;

    vector<int> C;
    C.push_back(0);
    C.push_back(2);
    C.push_back(0);
    cout << solution.threeSumMulti(C, 2) << endl;

    vector<int> D;
    D.push_back(0);
    D.push_back(2);
    D.push_back(3);
    D.push_back(2);
    cout << solution.threeSumMulti(D, 5) << endl;
}