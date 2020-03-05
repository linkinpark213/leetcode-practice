#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        while (m > 0 || n > 0) {
            if (m == 0 || n > 0 && A[m - 1] <= B[n - 1]) A[m + n] = B[--n];
            else A[m + n] = A[--m];
        }
    }
};

int main() {
    Solution solution;
    vector<int> A = {1, 2, 3, 0, 0, 0};
    vector<int> B = {2, 5, 6};
    solution.merge(A, 3, B, 3);
    for (auto it = A.begin(); it != A.end(); it++) cout << *it << " ";
    cout << endl;
    return 0;
}