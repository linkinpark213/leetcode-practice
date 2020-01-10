//
// Created by linkinpark213 on 2020/1/5.
//
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Trie {
public:
    int count;
    bool isLeaf;
    map<char, Trie*> children;

    Trie() {
        this->count = 0;
        this->isLeaf = false;
        this->children = map<char, Trie*>();
    }

    Trie(vector<string> products) {
        this->count = 0;
        this->isLeaf = false;
        this->children = map<char, Trie*>();
        for (const string &product : products) {
            this->add(product, 0);
        }
    }

    void add(const string &word, int pos) {
        this->count++;
        if (pos < word.size()) {
            char c = word[pos];
            Trie* child = this->children[c];
            if (child == NULL) {
                this->children[c] = new Trie();
                child = this->children[c];
            }
            child->add(word, pos + 1);
        } else {
            this->isLeaf = true;
        }
    }

    void search(string &searchWord, int pos, vector<string> &results) {
        if (results.size() >= 3) {
            return;
        }
        int size = static_cast<int>(searchWord.size());
        if (pos < size) {
            Trie* child = this->children[searchWord[pos]];
            if (child != NULL)
                child->search(searchWord, pos + 1, results);
        } else if (pos == size) {
            if (this->isLeaf) {
                results.push_back(searchWord);
            }
            this->dfs(searchWord, results);
            return;
        }
    }

    void dfs(string prefix, vector<string> &results) {
        if (results.size() >= 3) {
            return;
        }
        for (char c = 'a'; c <= 'z'; c++) {
            if (results.size() >= 3) {
                return;
            }
            auto iterator = this->children.find(c);
            if (iterator == this->children.end()) continue;
            else {
                Trie* child = iterator->second;
                if (child->isLeaf)
                    results.push_back(prefix + c);
                child->dfs(prefix + c, results);
            }
        }
    }
};

class Solution {
public:
    vector<vector<string> > suggestedProducts(vector<string> &products, string &searchWord) {
        vector<vector<string> > results;
        Trie root(products);
        for (unsigned int i = 1; i <= searchWord.size(); i++) {
            string word = searchWord.substr(0, i);
            vector<string> resultSingle;
            root.search(word, 0, resultSingle);
            results.push_back(resultSingle);
        }
        return results;
    }
};

int main() {
    Solution solution;
    vector<string> products;
    products.push_back("mobile");
    products.push_back("mouse");
    products.push_back("moneypot");
    products.push_back("monitor");
    products.push_back("mousepad");
    string searchWord = "mouse";
    vector<vector<string> > result = solution.suggestedProducts(products, searchWord);
    for (vector<string> v : result) {
        for (string &s : v) {
            cout << s << " ";
        }
        cout << endl;
    }
    return 0;
}