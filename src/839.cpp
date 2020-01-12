#include <iostream>
#include <vector>

using namespace std;

class Solution {
    bool isSimilar(string& x, string& y) {
        if (x.size() != y.size()) return false;
        int diff[2];
        int count = 0;
        for (int i = 0; i < x.size(); i++) {
            if (x[i] != y[i]) {
                count++;
                if (count > 2) return false;
                diff[count - 1] = i;
            }
        }
        if (count != 2 && count != 0) return false;
        if (x[diff[0]] == y[diff[1]] || x[diff[1] == y[diff[0]]])
            return true;
        return false;
    }
    
    void infect(int pos, int id, vector<int>& ids, bool* similarities, int length) {
        ids[pos] = id;
        for (int i = 0; i < length; i++) {
            if (similarities[pos * length + i] && ids[i] == -1) {
                infect(i, id, ids, similarities, length);
            }
        }
    }

public:
    int numSimilarGroups(vector<string>& A) {
        int id = 0, ptr = 0, length = A.size();
        bool similarities[length * length];
        for (int i = 0; i < length; i++) {
            similarities[i * length + i] = false;
            for (int j = i + 1; j < length; j++) {
                similarities[i * length + j] = isSimilar(A[i], A[j]);
                similarities[j * length + i] = similarities[i * length + j];
            }
        }
        vector<int> ids(length, -1);
        while (ptr < length) {
            if (ids[ptr] == -1) {
                infect(ptr, id, ids, similarities, length);
                id++;
            }
            ptr++;
        }
        return id;
    }
};

int main() {
    Solution solution;
    vector<string> A = {"tars","rats","arts","star"};
    cout << solution.numSimilarGroups(A) << endl;
    return 0;
}