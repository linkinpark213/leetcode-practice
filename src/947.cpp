#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class UnionFind {
   public:
    vector<int> parents;
    UnionFind(vector<vector<int>>& stones) {
        this->parents = vector<int>(stones.size(), -1);
        for (int i = 0; i < stones.size(); i++) {
            this->parents[i] = i;
        }
        for (int i = 0; i < stones.size(); i++) {
            for (int j = 0; j < stones.size(); j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    merge(i, j);
                }
            }
        }
    }

    int findRoot(int ind) {
        int root = ind;
        while (this->parents[root] != root) root = parents[root];
        int ptr = ind;
        while (ptr != root) {
            ind = this->parents[ptr];
            this->parents[ptr] = root;
            ptr = ind;
        }
        return root;
    }

    void merge(int a, int b) {
        a = findRoot(a);
        b = findRoot(b);
        if (a != b) parents[b] = a;
    }
};

class Solution {
   public:
    int removeStones(vector<vector<int>>& stones) {
        UnionFind collection(stones);
        int count = 0;
        unordered_set<int> roots;
        for (int i = 0; i < stones.size(); i++) {
            if (roots.find(collection.findRoot(i)) == roots.end()) { 
                count++;
                roots.insert(collection.findRoot(i));
            }
        }
        return stones.size() - count;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> stones;
    stones.push_back({0, 0});
    stones.push_back({0, 2});
    stones.push_back({1, 1});
    stones.push_back({0, 2});
    stones.push_back({2, 0});
    cout << solution.removeStones(stones);
    return 0;
}